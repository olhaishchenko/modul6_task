#!/usr/bin/python3
import os
import sys
from pathlib import Path
from shutil import move, unpack_archive

START_FOLDER = sys.argv[1] if len(sys.argv)>1 else "/Users/olha/Downloads/Test"
print(START_FOLDER)

# check START_FOLDER exist and a folder

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


def normalize_file(i):
    # TODO
    pass

def sort(now_folder):
    p=Path(now_folder)

    for i in p.iterdir():
        if i.is_dir():
            if i.name not in ('images' ,'documents','audio','video','archives','other'):
                sort(i)

        if i.is_file():
            normalize_file(i)

            if i.suffix.lower() in ('.jpeg', '.png', '.jpg', '.svg'):
                move(i,Path(IMAGE_PATH + '/' + i.name))

            elif i.suffix.lower() in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'):
                move(i,Path(DOCUMENT_PATH + '/' + i.name))

            elif i.suffix.lower() in ('.mp3', '.ogg', '.wav', '.amr'):
                move(i, Path(AUDIO_PATH + '/' + i.name))

            elif i.suffix.lower() in ('.avi', '.mp4', '.mov', '.mkv'):
                move(i, VIDEO_PATH + '/' + i.name)
    
            elif i.suffix.lower() in ('.zip', '.gz', '.tar'):
                Path(ARCHIVES_PATH + '/' + i.stem).mkdir()
                unpack_archive(i, ARCHIVES_PATH + '/' + i.stem)
                os.remove(i)

            else:
                move(i,OTHER_PATH + '/' + i.name)
        
        if i.is_dir():
            if i.name not in ('images' ,'documents','audio','video','archives','other'):
                Path(i).rmdir()
        

if __name__ == "__main__":
    sort(START_FOLDER)