import streamlit as st
from translatepy import Translator


translator = Translator()

st.title("App Tradutor")

texto = st.text_input(label='Insira o texto para tradução', value="olá")
detect_language = translator.language(texto).result
st.write(f'Idioma detectado: {detect_language.name}')


idiomas = ['ARABIAN','CHINESE','COREAN', 'ENGLISH', 'FRANÇAIS', 'GERMAN', 'HINDI', 'INDONESIAN','ITALIAN', 'JAPAN', 'LATIN','PORTUGUESE', 'RUSSIAN', 'SPAIN', 'TURCO']
choice = st.selectbox('Selecione o idioma para tradução: ', idiomas)

def translate(texto, idioma):
    global traducao
    traducao = translator.translate(texto, idioma).result
    return traducao

st.write('Tradução:', translate(texto, choice))

result = translator.text_to_speech(traducao)
with open("outputTR.mp3", "wb") as output:
    output.write(result.result)
    
audio_file = open('outputTR.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

