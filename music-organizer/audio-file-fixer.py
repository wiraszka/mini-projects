# Cleans up audio file names and tags
import os
import mutagen
import re
from mutagen import MutagenError
from mutagen.mp3 import MP3

root = "C:/Users/Adam/Desktop/Projects/music/music_sample"
all_tags = []

def get_tags(filename, song):
# Retrieves relevant file tags, then puts them in usable format
    tags = {
        'artist' : '',
        'title' : '',
        'album' : '',
        'genre' : '',
        'bpm' : '',
        'duration' : '',
        'bitrate' : '',
        }
    info = mutagen.File(filename, easy=True)
    for key in tags.keys():
        if key in info.keys():
            tags[key] = info.get(key)[0]
        if key not in info.keys():
            tags[key] = "None"

    extra_info = MP3(filename)
    tags['duration'] = extra_info.info.length
    tags['bitrate'] = extra_info.info.bitrate

    print(tags)
    all_tags.append(tags)
    return all_tags, tags

def format_file(all_tags):
    for tags in all_tags:
        if 'feat.' in tags['title']:
            print(tags['title'])
            split = tags['title'].split('feat')
            tags['title'] = re.sub('.+(feat).+', '.+(Feat.).+', tags['title'])
            print(tags['title'])
    return all_tags

for song in os.listdir(root):
    if song.endswith((".mp3",".m4a",".flac",".alac")):
        try:
            filename = root + "/" + song
            get_tags(filename, song)

        except MutagenError:
            print("error")
    format_file(all_tags)
