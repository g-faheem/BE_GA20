import librosa
import joblib
import soundfile
import os, glob, pickle
import numpy as np
import soundfile as soundfile


import warnings
warnings.filterwarnings("ignore")



#Extract features values like (mfcc, chroma, mel) from a single sound file

def extract_feature(file_name):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        stft = np.abs(librosa.stft(X))  # short time fourier transform for  pitch detection

        result = np.array([])

        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        result = np.hstack((result, mfccs))

        chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
        result = np.hstack((result, chroma))

        mel = np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate).T,axis=0)
        result = np.hstack((result, mel))

    return result



neutral = ['calm', 'neutral', 'surprised']
negative = ['angry','fearful','disgust','sad']

def three_emotion(emotion):
    if neutral.count(emotion)==1: #we return neutral if we find any emotion in the neutral list
        return 'neutral'
    elif negative.count(emotion) == 1:  # same but for negative list
        return 'negative'
    else:
        return 'positive' #we return positive as it is only left

def voice_emotion_pred():
    #Emotions in the RAVDESS dataset
    emotions={
      '01':'neutral', #neutral=calm, neutral, surprised
      '02':'calm', #positive=happy
      '03':'happy', #negative=angry,fearful,disgust,sad
      '04':'sad',
      '05':'angry',
      '06':'fearful',
      '07':'disgust',
      '08':'surprised'
    }

    vc_model = joblib.load("emotion_model.pkl")
    path = "C:/Users/princ/PycharmProjects/EmoReg/Modules/voice_model/sample.wav"

    data = extract_feature(path)


    print(vc_model.predict(data))


    return 'hello'

print(voice_emotion_pred())