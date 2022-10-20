#!/usr/bin/python3
import os
import sys
from pathlib import Path
import re
from shutil import move, unpack_archive

START_FOLDER = sys.argv[1] if len(sys.argv)>1 else "/Users"
print(START_FOLDER)

if Path(START_FOLDER).exists:
    pass
else:
    print('Folder not exists')
    exit(1)

IMAGE_PATH = START_FOLDER+'/images'
DOCUMENT_PATH = START_FOLDER+'/documents'
AUDIO_PATH = START_FOLDER+'/audio'
VIDEO_PATH = START_FOLDER+'/video'
ARCHIVES_PATH = START_FOLDER+'/archives'
OTHER_PATH = START_FOLDER+'/other'

Path(IMAGE_PATH).mkdir(exist_ok=True)
Path(DOCUMENT_PATH).mkdir(exist_ok=True)
Path(AUDIO_PATH).mkdir(exist_ok=True)
Path(VIDEO_PATH).mkdir(exist_ok=True)
Path(ARCHIVES_PATH).mkdir(exist_ok=True)
Path(OTHER_PATH).mkdir(exist_ok=True)

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize_name(name):
    new_name =''
    for char in name:
        if re.search(r'[0-9A-z]',char):
            char = char
        elif re.search(r'[А-Яа-яёєіїґ]',char):
            char = TRANS[ord(char)]
        else:
            char = '_'
        new_name += char
    return new_name
image_list = []
document_list = []
audio_list = []
video_list = []
archives_list = []
other_list = []
suffixes_list = set()
other_suffixes_list = set()

def sort(now_folder):
    p=Path(now_folder)

    for i in p.iterdir():
        if i.is_dir():
            if i.name not in ('images' ,'documents','audio','video','archives','other'):
                sort(i)

        if i.is_file():

            if i.suffix.lower() in ('.jpeg', '.png', '.jpg', '.svg'):
                image_list.append(normalize_name(i.stem)+i.suffix)
                suffixes_list.add(i.suffix)
                move(i, IMAGE_PATH + '/' + normalize_name(i.stem)+i.suffix)

            elif i.suffix.lower() in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', '.ppt'):
                document_list.append(normalize_name(i.stem)+i.suffix)
                suffixes_list.add(i.suffix)
                move(i, DOCUMENT_PATH + '/' + normalize_name(i.stem)+i.suffix)

            elif i.suffix.lower() in ('.mp3', '.ogg', '.wav', '.amr'):                
                audio_list.append(normalize_name(i.stem)+i.suffix)
                suffixes_list.add(i.suffix)
                move(i, AUDIO_PATH + '/' + normalize_name(i.stem)+i.suffix)

            elif i.suffix.lower() in ('.avi', '.mp4', '.mov', '.mkv'):
                video_list.append(normalize_name(i.stem)+i.suffix)
                suffixes_list.add(i.suffix)
                move(i, VIDEO_PATH + '/' + normalize_name(i.stem)+i.suffix)
    
            elif i.suffix.lower() in ('.zip', '.gz', '.tar'):
                archives_list.append(normalize_name(i.stem)+i.suffix) 
                suffixes_list.add(i.suffix)              
                unpack_archive(i, ARCHIVES_PATH + '/' + normalize_name(i.stem))
                os.remove(i)

            else:
                other_list.append(i.name)
                other_suffixes_list.add(i.suffix)
                move(i,OTHER_PATH + '/' + i.name)
        
        if i.is_dir():
            if i.name not in ('images' ,'documents','audio','video','archives','other'):
                Path(i).rmdir()

if __name__ == "__main__":
    sort(START_FOLDER)

print(f'''\n
            image_list={image_list}\n
            document_list={document_list}\n
            audio_list={audio_list}\n
            video_list={video_list}\n
            archives_list={archives_list}\n
            other_list={other_list}\n
            suffixes_list={suffixes_list}\n
            other_suffixes_list={other_suffixes_list}\n''')
