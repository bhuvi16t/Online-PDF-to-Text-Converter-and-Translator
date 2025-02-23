from flask import Flask, render_template, request, redirect, url_for, flash
from PyPDF2 import PdfReader
from googletrans import Translator
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "supersecretkey"

# Configure upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Main page
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # Handle PDF upload
        if 'pdf_file' not in request.files:
            flash('No file uploaded')
            return redirect(request.url)
        file = request.files['pdf_file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file and file.filename.endswith('.pdf'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Extract text from PDF
            reader = PdfReader(filepath)
            text = ''
            for page in reader.pages:
                text += page.extract_text()

            # Translate text
            translator = Translator()
            dest_lang = request.form['language']
            translated = translator.translate(text, dest=dest_lang)
            return render_template('index.html', translated_text=translated.text)
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)