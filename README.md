# PDF Translator using Flask

## Project Description
This project is a **web-based PDF Translator** that allows users to upload a PDF file, extract text from it, and translate the text into a selected language. The project is built using **Flask** for the backend and **HTML, CSS (Bootstrap), and JavaScript** for the frontend, ensuring a user-friendly and visually appealing interface.

## Features
✅ **Upload PDF** - Users can upload a PDF file for translation.  
✅ **Extract Text** - Extracts text from the uploaded PDF using **PyPDF2**.  
✅ **Translate Text** - Uses the **Google Translator API** to translate text into various languages.  
✅ **Multiple Language Support** - Supports translation into **Spanish, French, German, Hindi, and Chinese**.  
✅ **User-Friendly Interface** - Clean and attractive UI designed with **Bootstrap** and custom CSS.  

## Technologies Used
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Libraries Used:**
  - `Flask` (Web Framework)
  - `PyPDF2` (PDF Text Extraction)
  - `googletrans` (Translation API)
- **Storage:** Local file storage for uploaded PDFs

## Installation and Setup
### Prerequisites
Ensure you have **Python 3.x** installed.

### Step 1: Clone the Repository
```sh
git clone https://github.com/your-username/pdf-translator-flask.git
cd pdf-translator-flask
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 4: Run the Application
```sh
python app.py
```

### Step 5: Access the Web App
Open your browser and go to:  
```sh
http://127.0.0.1:5000/
```

## Project Structure
```
/pdf-translator-flask
│── app.py  (Flask Backend)
│── /uploads  (Folder for uploaded PDFs)
│── /templates  (HTML Templates)
│   ├── main.html  (Frontend UI)
│── /static  (CSS and assets)
│   ├── style.css  (Custom Styles)
│── requirements.txt  (Project Dependencies)
│── README.md  (Project Documentation)
```

## Usage Guide
1. Upload a **PDF file**.
2. Select a **target language** from the dropdown menu.
3. Click the **Translate** button.
4. View the **translated text** on the screen.

## Future Enhancements
🚀 Add support for **more file formats (DOCX, TXT, etc.)**.  
🚀 Implement **speech-to-text conversion** for PDFs with scanned images.  
🚀 Improve **translation accuracy** using AI-based models.  

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements.

## License
This project is open-source and available under the **MIT License**.

---
### 🌍 Happy Translating! 🚀
