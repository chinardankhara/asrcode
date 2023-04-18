import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
import os

input_file = "test.flac"
output_file = "test.wav"

audio = AudioSegment.from_file(input_file, format="flac")

audio.export(output_file, format="wav")

# Set the Azure Speech-to-Text subscription key and endpoint
speech_key = "cdfcf14879234603ab121b2b0e6237a9"
service_region = "eastus"

# Create a SpeechRecognizer object
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_config = speechsdk.audio.AudioConfig(filename="test.wav")
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# Perform speech recognition on the audio file
result = speech_recognizer.recognize_once()

# Print the transcribed text
print(result.text)
