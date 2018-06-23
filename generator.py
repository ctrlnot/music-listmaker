import os
import math
import errno
import config

class Generator:
  total = 0
  subdirs = []
  output_path = None

  def __init__(self, root):
    self.initialize(root)

  def initialize(self, dir_):
    self.find_subdirs(dir_)
    self.create_generator_folder()
    self.output_path = '{}/{}.txt'.format(config.generator_folder, config.output_filename)

  def find_subdirs(self, folder_path):
    dir_ = os.listdir(folder_path)

    for file_ in dir_:
      file_path = os.path.join(folder_path, file_)

      if os.path.isdir(file_path):
        self.subdirs.append(file_path)
        self.find_subdirs(file_path)

  def list_files(self):
    with open(self.output_path, 'w', encoding = "utf-8") as output_file:
      for dir_ in self.subdirs:
        files = os.listdir(dir_)
        dir_name = os.path.basename(os.path.normpath(dir_))
        dir_text = self.addPadding(dir_name) + '\n\n'

        output_file.write(dir_text)

        for file_ in files:
          title = file_ + '\n\n'

          if file_.endswith(config.audio_file_types):
            output_file.write(title)
            self.total += 1
    
    output_file.closed

  def create_generator_folder(self):
    try:
      os.makedirs(config.generator_folder)
    except OSError as e:
      if e.errno != errno.EEXIST:
        raise

  def addPadding(self, dirName):
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
