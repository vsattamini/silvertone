from audio_formating import Silvertone
from glob import glob
from google.colab import drive
import numpy as np
import pandas as pd
import os

from glob import glob
from google.colab import drive
import numpy as np

# os.chdir('/content/drive/MyDrive/Colab Notebooks')



def extract_ravdess(mels=256):
    '''
    Extracts audio features from ravdess db using methods defined in the
    Silvertone object
    '''
    wave = []
    spec = []
    id = []
    spectral_centroid = []
    mfcc = []
    chroma_stft = []
    tonnetz = []
    source = []
    emotion = []
    intensity = []
    repetition = []
    actor_gender = []
    actor_age = []

    speech = glob("/content/drive/MyDrive/Emotion Datasets/Emotion Datasets/Audio/RAVDESS/Audio_Speech_Actors_01-24/*.wav")

    for i in np.arange(0, len(speech)):
      tone = Silvertone(speech[i], mels)
      spec.append(tone.S_db_mel)
      wave.append(tone.x)
      spectral_centroid.append(tone.spectral_centroid)
      mfcc.append(tone.mfcc)
      chroma_stft.append(tone.chroma_stft)
      tonnetz.append(tone.tonnetz)
      id.append(speech[i][-24:-4])
      source.append('ravdess')
      emotion.append(speech[i][-17:-16])
      intensity.append(speech[i][-14:-13])
      repetition.append(speech[i][-8:-7])
      if speech[i][-8:-7] % 2 == 0 or speech[i][-8:-7] == 0:
          actor_gender.append('female')
      else:
          actor_gender.append('male')

    dic = {"id": id,"wave": wave,
       "spec": spec, "spectral_centroid": spectral_centroid,
       "mfcc": mfcc, "chroma_stft": chroma_stft, "tonnetz": tonnetz,
       "emotion":emotion, "intensity": intensity, "repetition": repetition,
       "actor_gender": actor_gender}
    df = pd.DataFrame(dic)

    emo_relation = {1: 'neutral', 2: 'calm', 3: 'happy', 4: 'sad',
            5: 'angry', 6: 'fearful', 7: 'disgust', 8: 'surprised'}
    int_relation = {2:3 ,1:2}


    df = df.replace({'emotion':emo_relation,'intensity':int_relation,})

    return df


def extract_crema(mels=256):
    '''
    Extracts audio features from crema db using methods defined in the
    Silvertone object
    '''
    wave = []
    spec = []
    id = []
    spectral_centroid = []
    mfcc = []
    chroma_stft = []
    tonnetz = []
    source = []
    emotion = []
    intensity = []
    actor_gender = []
    actor_age = []
    demo = pd.read_csv('demographic_relation.csv')

    speech = glob("/content/drive/MyDrive/Emotion Datasets/Emotion Datasets/Audio/Crema (avail in TFDS)/*.wav")
    repetition = np.arange(0,len(speech))

    for i in np.arange(0, len(speech)):
      tone = Silvertone(speech[i], mels)
      spec.append(tone.S_db_mel)
      wave.append(tone.x)
      spectral_centroid.append(tone.spectral_centroid)
      mfcc.append(tone.mfcc)
      chroma_stft.append(tone.chroma_stft)
      tonnetz.append(tone.tonnetz)
      id.append(speech[i][-19:-4])
      source.append('crema')
      emotion.append(speech[i][-10:-7])
      intensity.append(speech[i][-14:-13])
      # repetition.append(speech[i][-8:-7])
      actor_gender.append(speech[i][-19:-15])
      actor_age.append(speech[i][-19:-15])


    dic = {"id": id,"wave": wave,
       "spec": spec, "spectral_centroid": spectral_centroid,
       "mfcc": mfcc, "chroma_stft": chroma_stft, "tonnetz": tonnetz,
       "emotion":emotion, "intensity": intensity, "repetition": repetition,
       "actor_gender": actor_gender,"actor_age": actor_age}
    df = pd.DataFrame(dic)

    emo_relation = {'NEU': 'neutral', 2: 'calm', 'HAP': 'happy', 'SAD': 'sad',
            'ANG': 'angry', 'FEA': 'fearful', 'DIS': 'disgust', 8: 'surprised'}
    int_relation = {'XX': 0, 'LO':1,'MD':2,'HI':3}
    actor_gender = []
    actor_age = []
    for i in df['actor_age']:
        actor_age.append(demo[demo['ActorID'] == i]['Age'])
    for i in df['actor_gender']:
        actor_age.append((demo[demo['ActorID'] == i]['Sex'].lower()))

    df['actor_age'] = actor_age
    df['actor_gender'] = actor_gender
    df = df.replace({'emotion':emo_relation,'intensity':int_relation,})

    return df

def extract_savee(mels=256):
    '''
    Extracts audio features from savee db using methods defined in the
    Silvertone object
    '''
    wave = []
    spec = []
    id = []
    spectral_centroid = []
    mfcc = []
    chroma_stft = []
    tonnetz = []
    source = []
    emotion = []
    intensity = []
    actor_gender = []
    actor_age = []

    speech = glob("/content/drive/MyDrive/Emotion Datasets/Emotion Datasets/Audio/Savee/*.wav")
    repetition = np.arange(0,len(speech))

    for i in np.arange(0, len(speech)):
      tone = Silvertone(speech[i], mels)
      spec.append(tone.S_db_mel)
      wave.append(tone.x)
      spectral_centroid.append(tone.spectral_centroid)
      mfcc.append(tone.mfcc)
      chroma_stft.append(tone.chroma_stft)
      tonnetz.append(tone.tonnetz)
      id.append(speech[i][-19:-4])
      source.append('savee')
      emotion.append(speech[i][-10:-7])
      intensity.append(speech[i][-14:-13])
      # repetition.append(speech[i][-8:-7])
      actor_gender.append('male')
      actor_age.append('young')


    dic = {"id": id,"wave": wave,
       "spec": spec, "spectral_centroid": spectral_centroid,
       "mfcc": mfcc, "chroma_stft": chroma_stft, "tonnetz": tonnetz,
       "emotion":emotion, "intensity": intensity, "repetition": repetition,
       "actor_gender": actor_gender,"actor_age": actor_age}
    df = pd.DataFrame(dic)

    emo_relation = {'NEU': 'neutral', 2: 'calm', 'HAP': 'happy', 'SAD': 'sad',
            'ANG': 'angry', 'FEA': 'fearful', 'DIS': 'disgust', 8: 'surprised'}
    int_relation = {'XX': 0, 'LO':1,'MD':2,'HI':3}
    actor_gender = []
    actor_age = []
    for i in df['actor_age']:
        actor_age.append(demo[demo['ActorID'] == i]['Age'])
    for i in df['actor_gender']:
        actor_age.append((demo[demo['ActorID'] == i]['Sex'].lower()))

    df['actor_age'] = actor_age
    df['actor_gender'] = actor_gender
    df = df.replace({'emotion':emo_relation,'intensity':int_relation,})

    return df
