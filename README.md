# Music Listmaker

Want to list your local music list to a txt file for no apparent reason? Try this :v

### Requirements

- Install python 

- Capable of reading and can type on keyboard

- Knows how to use command line

### How to use

1. Download this repo (obviously).

2. Open `config.py` to any text editor (e.g. notepad)

3. On 2rd line write your music directory path (single quotes are necessary)
    > music_directory = 'C:\Users\pc\Music'

4. On 5st line write the folder where the generated txt file will be put (single quotes are still necessary)
    > generator_folder = 'generated'
    
5. On 8nd line write the generated txt file name (still same smh...)
    > output_filename = 'my-music'

6. On 14rd line, if for some reason, some of your music file types are not included on the list, just add it thank.
    > audio_file_types = ('.mp3', '.m4a', '.flac', '.wav', '.yourweirdmusicfiletype')

7. Generating:

    - Windows: Just run the `run.bat`
      1. Don't panic if there's some hacker thingy pops out. Just close it.

    - Others:
      1. Open terminal.
      2. Go to the where you put this repo of course.
      3. Run `python generate.py`

8. Hopefully, if everything worked out there should be a new folder inside this repo where the generated txt file is inside. Else, uhh goodluck!
