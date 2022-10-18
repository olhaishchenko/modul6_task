import os
import re
import sys
from pathlib import Path
from shutil import move

START_FOLDER = sys.argv[1] if len(sys.argv)>1 else "/Users/olha/Downloads/Test"

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

def normalize_name_file(file_name):
    l = Path(file_name).stem
    k = Path(file_name).parent
    normal_name=normalize_name(l)+Path(file_name).suffix
    new_direct= k + '/' + normal_name
    # new_direct= os.path.split(Path(file_name))[0]+'/'+normal_name
    move(file_name, new_direct)
    return new_direct

def sort(now_folder):
    p=Path(now_folder)

    for i in p.iterdir():
        # if i.is_dir():
        #     if i.name not in ('images' ,'documents','audio','video','archives','other'):
        #         sort(i)

        if i.is_file():
            i = normalize_name_file(i)
            print(i)

sort(START_FOLDER)