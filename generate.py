from generator import Generator
from config import music_directory

music_list = Generator(music_directory)
music_list.list_files()
print('Total music files listed: {}'.format(music_list.total))
