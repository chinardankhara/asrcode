import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
import os
import time
import string

def get_azure(filename):
    audio = AudioSegment.from_file(filename, format="flac")
    duration = round(len(audio) / 1000, 2)
    output_file = filename.split('.')[0] + '.wav'
    audio.export(output_file, format="wav")

    # Set the Azure Speech-to-Text subscription key and endpoint
    speech_key = "cdfcf14879234603ab121b2b0e6237a9"
    service_region = "eastus"

    start = time.time()
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    audio_config = speechsdk.audio.AudioConfig(filename=output_file)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = (speech_recognizer.recognize_once()).text
    end = time.time()

    result = result.translate(str.maketrans('', '', string.punctuation))
    result = result.upper()

    with open(filename.split('.')[0][:-5] + '-azure.txt', 'a') as f:
        f.write(filename.split('.')[0])
        f.write(', ')
        f.write(result)
        f.write(', ')
        f.write(str(round(end - start, 2)))
        f.write(', ')
        f.write(str(round((round(end - start, 2) / duration), 2)))
        f.write('\n')
