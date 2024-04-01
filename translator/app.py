# from flask import Flask, render_template, request
# from googletrans import Translator
# from languages import *

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html', languages=languages)

# @app.route('/translate', methods=['POST'])
# def translate():
#     if request.method == 'POST':
#         source_text = request.form['source_text']
#         target_language = request.form['target_language']
#         translator = Translator()
#         out = translator.translate(source_text, dest=target_language)
#         translated_text = out.text
#         return render_template('index.html', languages=languages, translated_text=translated_text)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
from googletrans import Translator
from languages import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', languages=languages, source_text='', translated_text='', target_language='')

@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        source_text = request.form['source_text']
        target_language = request.form['target_language']
        translator = Translator()
        out = translator.translate(source_text, dest=target_language)
        translated_text = out.text
        return render_template('index.html', languages=languages, source_text=source_text, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)