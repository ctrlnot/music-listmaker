import os
import errno
import config
# from config import audio_file_types
# from config import generator_folder

class Generator:
  total = 0
  subdirs = []
  output_file = None

  def __init__(self, root):
    self.create_generator_folder()
    self.find_subdirs(root)

    self.list_files()

  def find_subdirs(self, folder_path):
    dir_ = os.listdir(folder_path)

    for file_ in dir_:
      file_path = os.path.join(folder_path, file_)

      if os.path.isdir(file_path):
        self.subdirs.append(file_path)
        self.find_subdirs(file_path)

  def list_files(self):
    self.create_generator_folder()

    with open(config.output_filename, 'w') as output_file:
      for dir_ in subdirs:
        files = os.listdir(dir_)

        for file_ in files:
          title = file_ + '\n'

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

  def get_subdirs(self):
    return sorted(self.subdirs)
