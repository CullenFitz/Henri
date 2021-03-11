from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound
import os

def speak(words):
    words = str(words)

    authenticator = IAMAuthenticator('aqCXJ3nty9eEknjae3MNIuuDAKkuCYlpADiGgbTt_PhK')
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/640b96e2-6de0-4371-91f6-9d5c70428c9a')


    with open('voice.mp3', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                words,
                voice='en-US_OliviaV3Voice',
                accept='audio/mp3',
            ).get_result().content)

    playsound('voice.mp3')
    os.remove('voice.mp3')




