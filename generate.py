import os
import config

mFile = open(config.txt_file, 'w', encoding = 'utf-8')

def generateList(musicPath):
  musicDir = os.listdir(musicPath)

  for music in musicDir:
    filePath = os.path.join(musicPath, music)

    if os.path.isdir(filePath):
      mFile.write('######################   ' + music + '   ######################' + '\n\n')

      generateList(filePath)
    else:
      fileExtension = os.path.splitext(filePath)[1]

      if fileExtension in config.audio_file_types:
        mFile.write(music + '\n\n')

generateList(config.music_directory)
