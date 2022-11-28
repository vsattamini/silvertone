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
#    # To play audio in frontend:
#    st.audio(audio)
#
#    # To save audio to a file:
#    wav_file = open("audio.mp3", "wb")
#    wav_file.write(audio.tobytes())
#    #sample, sr = librosa.load(audio)
#    #ipd.Audio(sample)
#    #sample,sr = librosa.core.load('audio.mp3')
#    #ipd.Audio(sample)
st.write("Record a 5 seconds audio!!!")
filename = None

audio_bytes = audio_recorder()

if audio_bytes:
    st.audio(audio_bytes, format='audio/wav')
    print(type(audio_bytes))
    data, samplerate = librosa.load(io.BytesIO(audio_bytes))
    st.text(len(data))
    st.text(type(data))
#    wav_file = open("audio.mp3", "wb")
#    wav_file.write(audio_bytes.tobytes())
    #sample,sr = librosa.core.load(audio_bytes)
    #ipd.Audio(sample)
    #audio = st.audio(audio_bytes, format="audio/wav")
    #st.markdown(audio_bytes)
    #scipy.io.wavfile.write(filename, rate, data)
    #filename = 'audio.wav'
    #pickle.dump(audio_bytes, open(filename, 'wb'))
    #urllib.request.urlretrieve('http://localhost:8501/media/ea89cb71a0175954e7bbaf5c2a00fec7717d2268080a96b03b3e24f8.wav', 'audio.wav')
    #ipd.Audio(filename)
    #ipd.Audio('audio.wav'[5])



#sample,sr = librosa.core.load(audio.wav)
#iipd.Audio(sample)
#
