import os
import time
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

# Import our custom database, machine learning, and crop knowledge modules
import db
import ml_engine
import crop_data

# Initialize Flask application
app = Flask(__name__)

# Secret key required for session flash messages
app.secret_key = 'cropcare-college-project-secret-key'

# Upload configuration
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB limit

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize SQLite database schema
db.init_db()


def allowed_file(filename):
    """Check if the uploaded file has a permitted image extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.errorhandler(RequestEntityTooLarge)
def handle_file_too_large(e):
    """Handle uploads that exceed the 10 MB limit gracefully."""
    flash("The uploaded file exceeds the 10 MB limit. Please upload a smaller image.", "error")
    return redirect(url_for('home'))


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Step 1 & 2 & 3:
    Home upload page and disease detection orchestrator.
    - GET: Renders upload interface with guidelines and preview.
    - POST: Validates leaf photo, runs ML inference, saves report to SQLite,
            and redirects to the detailed Results Page.
    """
    if request.method == 'POST':
        # 1. Check for file part
        if 'file' not in request.files:
            flash("No file part found in request. Please select an image.", "error")
            return redirect(request.url)

        file = request.files['file']

        # 2. Check if user clicked detect without choosing a file
        if file.filename == '':
            flash("No file was selected. Please choose a crop leaf image.", "error")
            return redirect(request.url)

        # 3. Check allowed extension
        if not allowed_file(file.filename):
            flash("Unsupported file format! Please upload a JPG, JPEG, PNG, or WEBP photo.", "error")
            return redirect(request.url)

        # 4. Save file securely with timestamp prefix
        clean_name = secure_filename(file.filename)
        timestamp = int(time.time())
        saved_filename = f"{timestamp}_{clean_name}"
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], saved_filename)
        file.save(save_path)

        # 5. Run AI disease detection through ML Engine
        prediction = ml_engine.predict_disease(save_path)

        # 6. Save detection record to SQLite database
        report_data = {
            'image_filename': saved_filename,
            'crop_name': prediction.get('crop_name', 'Unknown Crop'),
            'disease_name': prediction.get('disease_name', 'Undetected'),
            'confidence': prediction.get('confidence', 0.0),
            'is_healthy': prediction.get('is_healthy', False),
            'status': prediction.get('status', 'completed'),
            'symptoms': prediction.get('symptoms', ''),
            'treatment': prediction.get('treatment', '')
        }
        report_id = db.save_report(report_data)

        # 7. Notify user and redirect to Results Page
        if prediction.get('status') == 'pending_model':
            flash("Image received! AI model inference is pending library setup (see instructions below).", "info")
        elif prediction.get('status') == 'unreliable':
            flash("Image processed. Diagnosis confidence is low; please verify photo quality.", "warning")
        else:
            flash("Crop leaf analyzed and report generated successfully!", "success")

        return redirect(url_for('view_result', report_id=report_id))

    return render_template('index.html')


@app.route('/result/<report_id>')
def view_result(report_id):
    """
    Step 4:
    Results Page displaying uploaded leaf image, crop name, diagnosis,
    confidence score, symptoms, treatments, and disclaimer.
    """
    report = db.get_report_by_id(report_id)
    if not report:
        flash(f"Report '{report_id}' was not found.", "error")
        return redirect(url_for('history'))

    return render_template('result.html', report=report)


@app.route('/crops')
def crops():
    """
    Crop Information Center:
    Displays comprehensive scientific names, growing conditions,
    common diseases, symptoms, prevention, and treatment/management
    for Rice, Tomato, Cotton, and Maize.
    Supports filtering by specific crop via query param (?crop=rice).
    """
    all_crops = crop_data.get_all_crops()
    crop_list = crop_data.get_crop_list()
    selected_crop_id = request.args.get('crop', default=None)
    selected_crop = crop_data.get_crop_by_id(selected_crop_id) if selected_crop_id else None

    return render_template(
        'crops.html',
        crops=all_crops,
        crop_list=crop_list,
        selected_crop=selected_crop,
        active_crop_id=selected_crop_id
    )


@app.route('/history')
def history():
    """
    Step 6:
    Detection History Page showing all previous detection reports from SQLite.
    """
    reports = db.get_all_reports()
    return render_template('history.html', reports=reports)


@app.route('/report/<report_id>')
def view_report(report_id):
    """
    Step 7:
    Downloadable and printable formal diagnostic report.
    """
    report = db.get_report_by_id(report_id)
    if not report:
        flash(f"Report '{report_id}' was not found.", "error")
        return redirect(url_for('history'))

    return render_template('report.html', report=report)


@app.route('/delete/<report_id>', methods=['POST'])
def delete_report_route(report_id):
    """
    Delete a detection report and remove its image file from uploads.
    """
    image_filename = db.delete_report(report_id)
    if image_filename:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
        if os.path.exists(image_path):
            try:
                os.remove(image_path)
            except OSError:
                pass  # Ignore if already removed

    flash(f"Report '{report_id}' has been deleted.", "info")
    return redirect(url_for('history'))


if __name__ == '__main__':
    app.run(debug=True)
