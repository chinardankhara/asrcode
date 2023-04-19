from deepgram import Deepgram
import asyncio
import time
import string

async def get_deepgram(filename):
    DEEPGRAM_API_KEY = '30651e81c45db3207413aa0018c1a0a52166fc55'
    MIMETYPE = 'audio/flac'
    FILE = filename
  # Initialize the Deepgram SDK
    deepgram = Deepgram(DEEPGRAM_API_KEY)

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
    with open(FILE.split('.')[0] + '-deepgram.txt', 'w') as f:
        temp = response["results"]["channels"][0]["alternatives"][0]["transcript"]
        #remove all the punctuation
        temp = temp.translate(str.maketrans('', '', string.punctuation))
        temp = temp.upper()
        f.write(temp)
        f.write('\n')
        f.write(str(responsetime))