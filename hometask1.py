#!/usr/bin/python3
import os
import sys
from pathlib import Path
from shutil import move

START_FOLDER = sys.argv[1] if len(sys.argv)>1 else "/Users/olha/Downloads/Test"
print(START_FOLDER)

# check START_FOLDER exist and a folder

IMAGE_PATH = START_FOLDER+'/images'
DOCUMENT_PATH = START_FOLDER+'/documents'

if not Path(IMAGE_PATH).exists():
    Path(IMAGE_PATH).mkdir()
if not Path(DOCUMENT_PATH).exists():
    Path(DOCUMENT_PATH).mkdir()
if not Path(START_FOLDER+'/audio').exists():
    Path(START_FOLDER+'/audio').mkdir()
if not Path(START_FOLDER+'/video').exists():
    Path(START_FOLDER+'/video').mkdir()
if not Path(START_FOLDER+'/archives').exists():
    Path(START_FOLDER+'/archives').mkdir()
if not Path(START_FOLDER+'/other').exists():
    Path(START_FOLDER+'/other').mkdir()


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
                move(i,Path(IMAGE_PATH+'/'+i.name))

            elif i.suffix.lower() in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'):
                move(i,Path(DOCUMENT_PATH+'/'+i.name))

            elif i.suffix.lower() in ('.mp3', '.ogg', '.wav', '.amr'):
                move(i,Path(START_FOLDER+'/audio/'+i.name))

            elif i.suffix.lower() in ('.avi', '.mp4', '.mov', '.mkv'):
                move(i,START_FOLDER+'/video/'+i.name)
    
            elif i.suffix.lower() in ('.zip', '.gz', '.tar'):
                move(i,START_FOLDER+'/archives/'+i.name)

            else:
                move(i,START_FOLDER+'/other/'+i.name)
        
        if i.is_dir():
            if i.name not in ('images' ,'documents','audio','video','archives','other'):
                Path(i).rmdir()
        

if __name__ == "__main__":
    sort(START_FOLDER)