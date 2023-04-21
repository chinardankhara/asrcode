os.chdir('./dev-other')
for filename in os.listdir():
    if filename != '.DS_Store':
        os.chdir(filename)
        for file in os.listdir():
            if file != '.DS_Store':
                os.chdir(file)
                for file in os.listdir():
                    if file.endswith('.flac'):
                        get_assembly(file)
                        get_openai(file)
                        get_azure(file)
                        await get_deepgram(file)
    os.chdir('../..')
