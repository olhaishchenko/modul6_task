from copy import copy
import os
import re
import sys
from pathlib import Path
from shutil import copyfile, move

START_FOLDER = sys.argv[1] if len(sys.argv)>1 else "/Users/olha/Downloads/Test"

CYRILLIC_SYMBOLS = "äабвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a","a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
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
    l=Path(file_name).name
    f=l.split('.')
    k=f[0]
    normal_name=normalize_name(k)+'.'+f[-1]
    (Path(os.getcwd()+'/'+normal_name))
    copyfile(file_name, Path(os.getcwd()+'/'+normal_name))
    return (Path(os.getcwd()+'/'+normal_name))

def sort(now_folder):
    p=Path(now_folder)

    for i in p.iterdir():
        if i.is_dir():
            if i.name not in ('images' ,'documents','audio','video','archives','other'):
                sort(i)

        if i.is_file():
            i = normalize_name_file(i)
            print(i)

sort(START_FOLDER)