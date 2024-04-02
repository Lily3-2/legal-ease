# from flask import Flask, render_template, request
# import pyttsx3
# import PyPDF2
# import threading

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/text_to_speech', methods=['POST'])
# def text_to_speech():
#     text = request.form['text']
#     speaker = pyttsx3.init()
#     speaker.say(text)
#     speaker.runAndWait()
#     return "Speech generated successfully"

# @app.route('/pdf_to_text', methods=['POST'])
# def pdf_to_text():
#     file = request.files['file']
#     page_range = request.form['page_range']
#     pages = page_range.split('-')
#     start_page = int(pages[0])
#     end_page = int(pages[1])
#     pdfReader = PyPDF2.PdfReader(file)
#     text = ""
#     for i in range(start_page - 1, end_page):
#         page = pdfReader.pages[i]
#         text += page.extract_text()
#     return text

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, send_file, Response
import tempfile
import pyttsx3
import PyPDF2
import io

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    text = request.form['text']
    rate = int(request.form['rate'])
    voice = request.form['voice']
    
    speaker = pyttsx3.init()
    speaker.setProperty('rate', rate)
    speaker.setProperty('voice', voice)
    speaker.say(text)
    speaker.runAndWait()
    
    return "Audio generated successfully"


@app.route('/pdf_to_speech', methods=['POST'])
def pdf_to_audio():
    file = request.files['file']
    start_page = int(request.form['start_page'])
    end_page = int(request.form['end_page'])
    rate = int(request.form['rate'])
    voice = request.form['voice']
    
    pdf_reader = PyPDF2.PdfReader(file)
    output_text = ""
    for page_number in range(start_page - 1, end_page):
        page = pdf_reader.pages[page_number]
        output_text += page.extract_text()
    
    speaker = pyttsx3.init()
    speaker.setProperty('rate', rate)
    speaker.setProperty('voice', voice)
    speaker.say(output_text)
    speaker.runAndWait()
    
    return "Audio generated successfully"


# Route to stop the audio playback
@app.route('/stop_audio', methods=['GET'])
def stop_audio():
    global stop_audio
    stop_audio = True
    return "Audio playback stopped"

if __name__ == '__main__':
    app.run(debug=True)

