import streamlit as st 
from googletrans import Translator
from languages import *


st.title("Translate To Your Language")
source_text = st.text_area("Enter text to translate:")
target_language = st.selectbox("Select target language:", languages)
translate = st.button('Translate')
if translate:
    translator = Translator()
    out = translator.translate(source_text, dest=target_language)
    translated_text = out.text
    translate_text = st.text_area("Translation:", value=translated_text)
    
                               







