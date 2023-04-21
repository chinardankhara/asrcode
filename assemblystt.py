import requests
import time
import string
from pydub import AudioSegment

def get_assembly(filename):
    UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
    TRANSCRIPTION_ENDPOINT = "https://api.assemblyai.com/v2/transcript"
    api_key = "INSERT"
    headers = {"authorization": api_key, "content-type": "application/json"}

    audio = AudioSegment.from_file(filename, format="flac")
    duration = round(len(audio) / 1000, 2)



    with open(filename, 'rb') as _file:
        data = _file.read()
    
    start = time.time()
    upload_response = requests.post(UPLOAD_ENDPOINT, headers=headers, data=data)
    audio_url = upload_response.json()["upload_url"]
    transcript_request = {'audio_url': audio_url}
    transcript_response = requests.post(TRANSCRIPTION_ENDPOINT, json=transcript_request, headers=headers)
    _id = transcript_response.json()["id"]

    while True:
        polling_response = requests.get(TRANSCRIPTION_ENDPOINT + "/" + _id, headers=headers)

        if polling_response.json()['status'] == 'completed':
            end = time.time()
            with open(filename.split('.')[0][:-5] + '-assembly.txt', 'a') as f:
                temp = polling_response.json()['text']
                temp = temp.translate(str.maketrans('', '', string.punctuation))
                temp = temp.upper()
                f.write(filename.split('.')[0])
                f.write(', ')
                f.write(temp)
                f.write(', ')
                f.write(str(round(end - start, 2)))
                f.write(', ')
                f.write(str(round((round(end - start, 2) / duration), 2)))
                f.write('\n')
            break
        elif polling_response.json()['status'] == 'error':
            raise Exception("Transcription failed. Make sure a valid API key has been used.")