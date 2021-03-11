"""speech_recognition has been installed"""
import speech_recognition as sr

def hear():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    words = r.recognize_google(audio)
    return words


