import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
import os
import time
import string

# input_file = "test.flac"
# output_file = "test.wav"

# audio = AudioSegment.from_file(input_file, format="flac")

# audio.export(output_file, format="wav")

# # Set the Azure Speech-to-Text subscription key and endpoint
# speech_key = "cdfcf14879234603ab121b2b0e6237a9"
# service_region = "eastus"

# # Create a SpeechRecognizer object
# speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
# audio_config = speechsdk.audio.AudioConfig(filename="test.wav")
# speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# # Perform speech recognition on the audio file
# result = speech_recognizer.recognize_once()

# # Print the transcribed text
# print(result.text)

def get_azure(filename):
    audio = AudioSegment.from_file(filename, format="flac")
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

    with open(filename.split('.')[0] + '-azure.txt', 'w') as f:
        f.write(result)
        f.write('\n')
        f.write(str(end - start))

