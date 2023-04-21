from deepgram import Deepgram
import asyncio
import time
import string
from pydub import AudioSegment

async def get_deepgram(filename):
    DEEPGRAM_API_KEY = 'INSERT'
    MIMETYPE = 'audio/flac'
    FILE = filename
  # Initialize the Deepgram SDK
    deepgram = Deepgram(DEEPGRAM_API_KEY)

    audio = AudioSegment.from_file(filename, format="flac")
    duration = round(len(audio) / 1000, 2)
    # file is local
    # Open the audio file
    audio = open(FILE, 'rb')

    # Set the source
    source = {
      'buffer': audio,
      'mimetype': MIMETYPE
    }

  # Send the audio to Deepgram and get the response
    start = time.time()
    response = await asyncio.create_task(deepgram.transcription.prerecorded(source,
    {'punctuate': True, 'model': 'nova',}))
    end = time.time()
    responsetime = end - start

  # write the response to the same file name but with txt extension
    with open((FILE.split('.')[0])[:-5] + '-deepgram.txt', 'a') as f:
        temp = response["results"]["channels"][0]["alternatives"][0]["transcript"]
        #remove all the punctuation
        temp = temp.translate(str.maketrans('', '', string.punctuation))
        temp = temp.upper()
        f.write(FILE.split('.')[0])
        f.write(', ')
        f.write(temp)
        f.write(', ')
        f.write(str(round(responsetime, 2)))
        f.write(', ')
        f.write(str(round((round(end - start, 2) / duration), 2)))
        f.write('\n')
        