# Music Directory
music_directory = 'E:\Music'

# Filename of text to be generated
# Note:
#   Created `generated` folder first.
#   The txt file is advised to store inside `generated` folder to be ignored by .gitignore
output_file = 'generated/music-list.txt'

# Temporary text file to store all music nested in folders inside music directory
nested_music_file = 'generated/inside-folder-music.txt'

# Temporary text file to store all music in the root/music directory
root_music_file = 'generated/inside-folder-music.txt'

# Expected audio file types
# Note:
#   The list is incomplete because he is lazy af to write all of them and to research more general solution
#   Just add if something isn't included 
audio_file_types = ['.mp3', '.m4a', '.flac', '.wav']
