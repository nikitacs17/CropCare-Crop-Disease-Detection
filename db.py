import sqlite3
import os
from datetime import datetime

# Path to the SQLite database in the project directory
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cropcare.db')


def get_db_connection():
    """Establish and return a connection to the SQLite database with Row factory."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Enables accessing columns by name like dict
    return conn


def init_db():
    """Initialize the database table for crop disease detection reports."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            report_id TEXT UNIQUE NOT NULL,
            created_at TEXT NOT NULL,
            image_filename TEXT NOT NULL,
            crop_name TEXT NOT NULL,
            disease_name TEXT NOT NULL,
            confidence REAL NOT NULL,
            is_healthy INTEGER NOT NULL DEFAULT 0,
            status TEXT NOT NULL DEFAULT 'completed',
            symptoms TEXT,
            treatment TEXT
        )
    ''')

    conn.commit()
    conn.close()


def generate_report_id():
    """Generate a readable, unique report ID, e.g., CC-20261025-4821."""
    timestamp = datetime.now().strftime("%Y%m%d")
    unique_suffix = str(int(datetime.now().timestamp() * 1000))[-4:]
    return f"CC-{timestamp}-{unique_suffix}"


def save_report(data):
    """
    Save a new detection report into the SQLite database.
    data: dict containing image_filename, crop_name, disease_name,
          confidence, is_healthy, status, symptoms, treatment.
    Returns: report_id
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    report_id = generate_report_id()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
        INSERT INTO reports (
            report_id, created_at, image_filename, crop_name,
            disease_name, confidence, is_healthy, status, symptoms, treatment
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        report_id,
        created_at,
        data.get('image_filename', ''),
        data.get('crop_name', 'Unknown Crop'),
        data.get('disease_name', 'Undetected'),
        float(data.get('confidence', 0.0)),
        1 if data.get('is_healthy') else 0,
        data.get('status', 'completed'),
        data.get('symptoms', 'No symptoms recorded.'),
        data.get('treatment', 'No specific treatment recommended.')
    ))

    conn.commit()
    conn.close()
    return report_id


def get_all_reports():
    """Retrieve all reports ordered by most recent first."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reports ORDER BY id DESC')
    reports = cursor.fetchall()
    conn.close()
    return reports


def get_report_by_id(report_id):
    """Retrieve a single detection report by its unique report_id."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reports WHERE report_id = ?', (report_id,))
    report = cursor.fetchone()
    conn.close()
    return report


def delete_report(report_id):
    """Delete a report record and return the deleted report's image filename for cleanup."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT image_filename FROM reports WHERE report_id = ?', (report_id,))
    row = cursor.fetchone()
    image_filename = row['image_filename'] if row else None

    cursor.execute('DELETE FROM reports WHERE report_id = ?', (report_id,))
    conn.commit()
    conn.close()
    return image_filename
