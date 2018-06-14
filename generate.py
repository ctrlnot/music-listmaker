import os
import config
import math

musicTotal = 0
mFile = open(config.txt_file, 'w', encoding = 'utf-8')

def generateList(musicPath):
  global musicTotal
  musicDir = os.listdir(musicPath)

  for music in musicDir:
    filePath = os.path.join(musicPath, music)

    if os.path.isdir(filePath):
      displayText = addPadding(music) + '\n\n'
      mFile.write(displayText)

      generateList(filePath)
    else:
      displayText = music + '\n\n'
      fileExtension = os.path.splitext(filePath)[1]

      if fileExtension in config.audio_file_types:
        musicTotal += 1
        mFile.write(displayText)

def addPadding(dirName):
  newDirName = '   ' + dirName + '   '
  pad = '#'
  dirLen = len(newDirName)

  maxLen = 75
  spaceLeft = (maxLen - dirLen) / 2
  leftPadLen = math.floor(spaceLeft)
  rightPadLen = int(spaceLeft)

  leftPad = pad.ljust(leftPadLen, pad)
  rightPad = pad.rjust(leftPadLen, pad)

  newDirName = leftPad + newDirName + rightPad

  return newDirName

generateList(config.music_directory)
print('Total music files listed: ' + str(musicTotal))
