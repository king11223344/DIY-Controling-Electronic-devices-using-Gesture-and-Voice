import os
from google.cloud import speech
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='key.json'
speech_client=speech.SpeechClient()