import openai
import time
import string
from pydub import AudioSegment

def get_openai(filename):
    audio = AudioSegment.from_file(filename, format="flac")
    duration = round(len(audio) / 1000, 2)
    output_file = filename.split('.')[0] + '.wav'
    audio.export(output_file, format="wav")

    openai.api_key = 'INSERT'

    with open (output_file, 'rb') as f:
        start = time.time()
        transcript = openai.Audio.transcribe("whisper-1", f)['text']
        end = time.time()
    
    transcript = transcript.translate(str.maketrans('', '', string.punctuation))
    transcript = transcript.upper()

    with open(filename.split('.')[0][:-5] + '-openai.txt', 'a') as f:
        f.write(filename.split('.')[0])
        f.write(', ')
        f.write(transcript)
        f.write(', ')
        f.write(str(round((end - start), 2)))
        f.write(', ')
        f.write(str(round((round(end - start, 2) / duration), 2)))
        f.write('\n')