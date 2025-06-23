import streamlit as st
import speech_recognition as sr


st.title('Speech to Text converter')

recog = sr.Recognizer()
mic = sr.Microphone()

with mic as source:


    st.write('speak now')
    audio = recog.listen(source)
    

    try:
        text = recog.recognize_google(audio)
        st.write(f'you said: {text}')

    except:
        st.write('could not understand audio')

    finally:
        st.write('process complete')

