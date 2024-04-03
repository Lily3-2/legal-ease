from flask import Flask, render_template, request
from googletrans import Translator
import PyPDF2
from languages import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', languages=languages, source_text='', translated_text='', target_language='')

@app.route('/translate', methods=['POST'])
def translate_text():
    if request.method == 'POST':
        source_text = request.form['source_text']
        target_language = request.form['target_language']
        translator = Translator()
        out = translator.translate(source_text, dest=target_language)
        translated_text = out.text
        return render_template('index.html', languages=languages, source_text=source_text, translated_text=translated_text)


@app.route('/translate-pdf', methods=['POST'])
def translate_pdf():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        if pdf_file.filename == '':
            return render_template('index.html', languages=languages, translated_text='Error: No file selected')
        
        target_language = request.form['target_language_pdf']
        pdf_text = extract_text_from_pdf(pdf_file)

        
        if pdf_text.strip() == '':
            return render_template('index.html', languages=languages, translated_text='Error: Empty PDF file')
        
        try:
            translator = Translator()
            out = translator.translate(pdf_text, dest=target_language)
            translated_text = out.text
            return render_template('index.html', languages=languages, translated_text=translated_text)
        except Exception as e:
            error_message = f"An error occurred while translating the PDF: {str(e)}"
            return render_template('index.html', languages=languages, translated_text=error_message)

# @app.route('/translate-pdf', methods=['POST'])
# def translate_pdf():
#     if request.method == 'POST':
#         pdf_file = request.files['pdf_file']
#         if pdf_file.filename == '':
#             return render_template('index.html', languages=languages, translated_text='Error: No file selected')
        
#         target_language = request.form['target_language_pdf']
#         pdf_text = extract_text_from_pdf(pdf_file)

        
#         if pdf_text.strip() == '':
#             return render_template('index.html', languages=languages, translated_text='Error: Empty PDF file')
        
#         translator = Translator()
#         out = translator.translate(pdf_text, dest=target_language)
#         translated_text = out.text
        
#         return render_template('index.html', languages=languages, translated_text=translated_text)

def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = pdf_reader.numPages
    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
    return text

if __name__ == '__main__':
    app.run(debug=True)