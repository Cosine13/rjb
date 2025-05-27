import speech_recognition as sr
import librosa
import numpy as np

class AudioAnalyzer:
    def __init__(self):
        self.r = sr.Recognizer()

    def transcribe_audio(self, audio_file_path):
        with sr.AudioFile(audio_file_path) as source:
            audio = self.r.record(source)
            try:
                text = self.r.recognize_google(audio, language='zh-CN')
                return text
            except sr.UnknownValueError:
                return ""
            except sr.RequestError as e:
                print(f"Error; {e}")
                return ""

    def analyze_audio_features(self, audio_file_path):
        y, sr = librosa.load(audio_file_path)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        pitch = librosa.yin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
        return {
            "mfccs": np.mean(mfccs, axis=1),
            "pitch": np.mean(pitch)
        }