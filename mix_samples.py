'''
Script to mix two testing samples
'''
import librosa
import numpy as np


# provide the wav name and mix
# speech1 = '/media/nca/data/raw_data/speech_train_r/FCMM0/TRAIN_DR2_FCMM0_SI1957.WAV'
# speech2 = '/media/nca/data/raw_data/speech_train_r/FKLC0/TRAIN_DR4_FKLC0_SX355.WAV'
speech1 = r'C:\Users\changjac\Google Drive\HP Intern\EE\cock_tailk_python\MaleSpeech-16-4-mono-20secs.wav'
speech2 = r'C:\Users\changjac\Google Drive\HP Intern\EE\cock_tailk_python\FemaleSpeech-16-4-mono-20secs.wav'

data1, _ = librosa.load(speech1, sr=8000)
data2, _ = librosa.load(speech2, sr=8000)
mix = data1[:len(data2)] + data2[:len(data1)]
librosa.output.write_wav(r'C:\Users\changjac\Google Drive\HP Intern\EE\deep-clustering-master\mix.wav', mix, 8000)
