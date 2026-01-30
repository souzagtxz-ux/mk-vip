import streamlit as st
from mtranslate import translate
import speech_recognition as sr

st.set_page_config(page_title="mk vip", page_icon="🎙️")
st.title("MK VIP - Tradutor de Áudio")

if st.button('OUVIR E TRADUZIR'):
    st.write("Ouvindo...")
    rec = sr.Recognizer()
    try:
        with sr.Microphone() as mic:
            audio = rec.listen(mic, timeout=5)
            texto = rec.recognize_google(audio, language='en-US')
            traducao = translate(texto, 'pt')
            st.success(f"Inglês: {texto}")
            st.info(f"Português: {traducao}")
    except Exception as e:
        st.error("Não consegui ouvir. Verifique o microfone.")
