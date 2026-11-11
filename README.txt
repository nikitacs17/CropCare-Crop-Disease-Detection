================================================================================
CROPCARE - AI-POWERED CROP DISEASE DETECTION & REPORTING SYSTEM
================================================================================
Academic Project Submission
Developed with Python, Flask, ONNX Runtime, and SQLite

--------------------------------------------------------------------------------
1. PROJECT OVERVIEW
--------------------------------------------------------------------------------
CropCare is an intelligent agricultural web application designed to help farmers 
and agronomists diagnose crop leaf diseases rapidly and accurately.

Key Features:
- Real-Time AI Disease Diagnosis: Analyzes uploaded leaf photos using a fine-tuned
  PlantVillage MobileNetV2 deep learning model running locally via ONNX Runtime.
- Diagnostic Results & Confidence Scoring: Displays predicted disease, 
  mathematical confidence percentage, health status, symptoms, and treatment plan.
- Crop Information Center: Detailed agronomic guides, optimal growing conditions,
  and comprehensive pathology profiles for Rice, Tomato, Cotton, and Maize.
- SQLite History Tracking: Automatically logs every diagnosis with timestamp, 
  leaf thumbnail, and clinical outcome.
- Official Printable Report: Generates a formal, printable/PDF diagnostic report 
  complete with signature blocks for extension officers and farmers.

--------------------------------------------------------------------------------
2. SYSTEM PREREQUISITES
--------------------------------------------------------------------------------
- Operating System: Windows 10 or Windows 11 (64-bit)
- Python: Version 3.10, 3.11, 3.12, 3.13, or 3.14 (64-bit)
- Code Editor: Visual Studio Code (or any terminal)
- Web Browser: Google Chrome, Microsoft Edge, or Mozilla Firefox
- Internet connection is only required during initial "pip install" to download packages.
  Once installed, the entire website and AI model run 100% OFFLINE without any external API keys.

--------------------------------------------------------------------------------
3. PROJECT FOLDER STRUCTURE
--------------------------------------------------------------------------------
cropcare/
├── app.py                      <- Flask web server and routing controller
├── crop_data.py                <- Knowledge base for Rice, Tomato, Cotton, and Maize
├── db.py                       <- SQLite database manager
├── ml_engine.py                <- AI computer vision inference & preprocessing engine
├── setup_model.py              <- Setup verification utility
├── cropcare.db                 <- SQLite database file (auto-created if missing)
├── requirements.txt            <- Python dependencies file
├── README.txt                  <- Step-by-step setup and running instructions
│
├── models/                     <- Machine learning model & labels
│   ├── crop_disease_model.onnx <- Pretrained MobileNetV2 ONNX model weights (8.8 MB)
│   ├── config.json             <- 38 PlantVillage disease class mappings
│   └── preprocessor_config.json<- Image normalization and resizing specifications
│
├── static/                     <- Static front-end assets
│   ├── css/
│   │   └── style.css           <- Agricultural green-and-white responsive theme
│   ├── js/
│   │   └── upload.js           <- Drag-and-drop file upload & live preview script
│   └── uploads/                <- Saved leaf photos uploaded by users
│
└── templates/                  <- Jinja2 HTML templates
    ├── base.html               <- Common layout, navigation, and alerts
    ├── index.html              <- Home leaf photo upload interface
    ├── crops.html              <- Crop Information Center with interactive tabs
    ├── result.html             <- Diagnostic result and treatment page
    ├── history.html            <- Detection history log and statistical summary
    └── report.html             <- Printable official diagnostic report

--------------------------------------------------------------------------------
4. STEP-BY-STEP SETUP & RUN INSTRUCTIONS (VS CODE ON WINDOWS)
--------------------------------------------------------------------------------

STEP 1: Extract the Project Folder
  - Unzip the submission archive to your computer (e.g., C:\Users\<YourName>\Desktop\cropcare).

STEP 2: Open in Visual Studio Code
  - Open VS Code.
  - Go to: File -> Open Folder...
  - Select the extracted "cropcare" folder.

STEP 3: Open the Integrated Terminal
  - In VS Code, open a new terminal: Terminal -> New Terminal (or press Ctrl + `).
  - Ensure the terminal is inside the "cropcare" directory.

STEP 4: Create a Python Virtual Environment
  In the terminal, run:
      python -m venv venv

STEP 5: Activate the Virtual Environment
  In PowerShell, run:
      .\venv\Scripts\Activate.ps1

  * Note: If PowerShell shows an "Execution Policy" restriction, run this first:
      Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    Then re-run:
      .\venv\Scripts\Activate.ps1

  * If using Command Prompt (cmd), run:
      venv\Scripts\activate.bat

  You will see "(venv)" appear at the start of your terminal prompt.

STEP 6: Install the Required Dependencies
  In the activated terminal, run:
      pip install -r requirements.txt

  This will automatically install Flask, Werkzeug, Pillow, NumPy, and ONNX Runtime.

STEP 7: (Optional) Verify AI Model & Dependencies
  In the terminal, run:
      python setup_model.py

  Expected Output:
      [OK] pillow is installed.
      [OK] numpy is installed.
      [OK] onnxruntime is installed.
      [OK] Trained model exists at: ...\models\crop_disease_model.onnx (8.80 MB)
      >>> System is 100% ready for real-time Crop Disease AI inference! <<<

STEP 8: Launch the Website
  In the terminal, run:
      python app.py

  Expected Output:
      * Serving Flask app 'app'
      * Debug mode: on
      * Running on http://127.0.0.1:5000

STEP 9: Access the Website in Your Browser
  - Open your browser and navigate to:
      http://127.0.0.1:5000

--------------------------------------------------------------------------------
5. HOW TO TEST & VERIFY EACH FEATURE
--------------------------------------------------------------------------------

1. AI DISEASE DETECTION:
   - On the Home page (http://127.0.0.1:5000), drag & drop or browse for a leaf photo.
   - You can test with any sample leaf photo located in "static/uploads/" or any 
     plant leaf photo (e.g., tomato, corn, apple leaf).
   - Click "Detect Crop Disease".
   - The website will process the leaf through the ONNX deep learning model and 
     redirect to the Result Page.
   - You will see the diagnosed crop name, disease name, confidence score (e.g., 92.5%),
     pathological symptoms, and recommended treatment protocols.

2. DOWNLOAD / PRINT REPORT:
   - On the Result Page, click "📄 Download / Print Report".
   - An official formal diagnostic sheet will open.
   - Click "🖨️ Print / Save as PDF" to generate or print the PDF.

3. DETECTION HISTORY:
   - Click "History" in the top navigation bar.
   - View the table containing all analyzed reports, confidence scores, dates, 
     and thumbnails. You can view or delete past records.

4. CROP INFORMATION CENTER:
   - Click "Crop Information" in the top navigation bar.
   - Browse the comprehensive agronomic guides and disease management protocols
     for Rice, Tomato, Cotton, and Maize.
   - Use the top crop tabs to filter between crops.

--------------------------------------------------------------------------------
6. TECHNICAL NOTES FOR THE EVALUATOR
--------------------------------------------------------------------------------
- Model Architecture: MobileNetV2 (1.0, 224 input resolution) fine-tuned on the 
  benchmark PlantVillage dataset (38 disease and healthy classes across 14 crops).
- Inference Engine: ONNX Runtime CPUExecutionProvider (runs locally on CPU in <50ms).
- Database: Embedded SQLite (cropcare.db). No external database server (MySQL/PostgreSQL) 
  is required, making the project 100% portable.
- Security: Uploaded filenames are sanitized using Werkzeug's secure_filename() 
  with timestamp prefixes to prevent collisions. Maximum upload size is 10 MB.
================================================================================
