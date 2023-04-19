import openai
import time
import string

def get_openai(filename):
    openai.api_key = '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'

    with open (filename, 'rb') as f:
        start = time.time()
        transcript = openai.Audio.transcribe("whisper-1", f)['text']
        end = time.time()
    
    transcript = transcript.translate(str.maketrans('', '', string.punctuation))
    transcript = transcript.upper()
    time = end - start

    with open(filename.split('.')[0] + '-openai.txt', 'w') as f:
        f.write(transcript)
        f.write('\n')
        f.write(str(time))