import os
import config
import math
import fileinput
from generator import Generator

musicTotal = 0
# outputFile = open(config.output_file, 'w', encoding = 'utf-8')
# insideFolderMusic = open(config.nested_music_file, 'w', encoding = 'utf-8')
# rootMusic = open(config.root_music_file, 'w', encoding = 'utf-8')

all_subdirs = []
# def find_subdirs(folder_path, dir_list = None):
  # global all_subdirs
  # dir_ = os.listdir(folder_path)

  # # Initialize list if empty
  # if dir_list is None:
  #   dir_list = []

  # for file_ in dir_:
  #   file_path = os.path.join(folder_path, file_)
    
  #   if os.path.isdir(file_path):
  #     all_subdirs.append(file_path)
  #     find_subdirs(file_path)



# def generateList(musicPath):
  # global musicTotal
  # musicDir = os.listdir(musicPath)

  # for music in musicDir:
  #   filePath = os.path.join(musicPath, music)
  #   parentDir = os.path.abspath(os.path.join(filePath, os.pardir))

  #   if os.path.isdir(filePath):
  #     displayText = addPadding(music) + '\n\n'
  #     insideFolderMusic.write(displayText)

  #     generateList(filePath)
  #   else:
  #     displayText = music + '\n\n'
  #     fileExtension = os.path.splitext(filePath)[1]

  #     if fileExtension in config.audio_file_types:
  #       musicTotal += 1
        
  #       if parentDir != config.music_directory:
  #         insideFolderMusic.write(displayText)
  #       else:
  #         rootMusic.write(displayText)

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

# def concatenateSources():
#   sources = [config.nested_music_file, config.root_music_file]
  
  # with open(config.output_file, 'w', encoding = 'utf-8') as outfile:
  #   for source in sources:
  #     with open(source) as infile:
  #       outfile.write(infile.read())
  # with open(config.output_file, 'w') as fout, fileinput.input(sources) as fin:
  #   for line in fin:
  #     fout.write(line)


# generateList(config.music_directory)
# concatenateSources()
# print('Total music files listed: ' + str(musicTotal))
# find_subdirs(config.music_directory)
# print(all_subdirs)

g = Generator(config.music_directory, config.output_file)
# print(g.get_subdirs())
# print(g.test())
