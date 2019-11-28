# Cleans up audio file names and tags
import os
import mutagen
from mutagen import MutagenError
from mutagen.mp3 import MP3

def check_tags(filename, song):
    info = mutagen.File(filename, easy=True)
    for tag in ['artist', 'album', 'title']:
        if tag not in info.keys():
            print(song, "has no", tag, "tag")
            return filename
        elif info[tag] == [u'']:
            return (song, "has an empty", tag, "tag")

root = "C:/Users/Adam/Desktop/Projects/music/music_sample"
for song in os.listdir(root):
    if song.endswith((".mp3",".m4a",".flac",".alac")):
        try:
            filename = root + "/" + song
            check_tags(filename, song)

        except MutagenError:
            print("error")
