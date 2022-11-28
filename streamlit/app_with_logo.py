import streamlit as st
import requests
import pandas as pd
import numpy as np
import librosa
from audio_recorder_streamlit import audio_recorder
from audiorecorder import audiorecorder
import pickle
import IPython.display as ipd
from scipy.io.wavfile import write
import io
#from io import BytesIO
#import urllib
#from pydub import AudioSegment


#st.title("Audio Recorder")
#audio = audiorecorder("Click to record", "Recording...")
#
#if len(audio) > 0:
#    # To play audiimport streamlit as st
import requests
import pandas as pd
import numpy as np
import librosa
from audio_recorder_streamlit import audio_recorder
from audiorecorder import audiorecorder
import pickle
import IPython.display as ipd
from scipy.io.wavfile import write
import pickle
import io
import os
import time




from datetime import datetime
filename = None
now = datetime.now() # current date and time
date_time = now.strftime("%Y_%m_%d_%H_%M_%S")
#print("date and time:",date_time
st.title("Silvertone!")
#st.header("Record a 5 seconds audio, and receive a % ....")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


st.sidebar.title("Welcome to Silvertone!")
st.sidebar.image("logo2.png", use_column_width=True)
st.sidebar.text("Contributors:")
st.sidebar.text("Luiz Lianza")
st.sidebar.text("Victor Sattamini ")
st.sidebar.text("Lucas Gama")
st.sidebar.text("Guilherme Barreto")


import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('logo2.png')


audio_bytes = audio_recorder()
if audio_bytes:
    st.audio(audio_bytes, format='audio/wav')
    filename = (f'{date_time}audio.pkl')
    #storage.child(path_on_cloud).push(audio_bytes)
    pickle.dump(audio_bytes, open(filename, 'wb'))

if filename is not None:
    with open(filename, 'rb') as f:
        audio_lib = pickle.load(f)
        data, samplerate = librosa.load(io.BytesIO(audio_lib))
        #col1, col2, col3,col4 = st.columns(4)
        #col1.metric("Happiness", "","34%")
        #col2.metric("Surprise", "9 %","34")
        #col3.metric("Neutral", "54%")
        #col4.metric("Sad", "1%")

        #st.markdown(len(data))
        os.remove(filename)
        #st.markdown(len(data))
        #st.markdown(type(data))
        #st.markdown(filename)



filename = None

audio_bytes = audio_recorder()

if audio_bytes:
    st.audio(audio_bytes, format='audio/wav')
    print(type(audio_bytes))
    data, samplerate = librosa.load(io.BytesIO(audio_bytes))
    st.text(len(data))
    st.text(type(data))
