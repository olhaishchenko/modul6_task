import os
from pathlib import Path
from shutil import move

begin = os.getcwd()
print(begin)

if not Path(begin+'/images').exists():
    Path(begin+'/images').mkdir()
if not Path(begin+'/documents').exists():
    Path(begin+'/documents').mkdir()
if not Path(begin+'/audio').exists():
    Path(begin+'/audio').mkdir()
if not Path(begin+'/video').exists():
    Path(begin+'/video').mkdir()
if not Path(begin+'/archives').exists():
    Path(begin+'/archives').mkdir()
if not Path(begin+'/other').exists():
    Path(begin+'/other').mkdir()


def sort(begin,now_folder):
    p=Path(now_folder)
    for i in p.iterdir():
        if i.is_file():
          
            if i.suffix.lower() in ('.jpeg', '.png', '.jpg', '.svg'):
                move(i,Path(begin+'/images/'+i.name))

            elif i.suffix.lower() in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'):
                move(i,Path(begin+'/documents/'+i.name))

            elif i.suffix.lower() in ('.mp3', '.ogg', '.wav', '.amr'):
                move(i,Path(begin+'/audio/'+i.name))

            elif i.suffix.lower() in ('.avi', '.mp4', '.mov', '.mkv'):
                move(i,begin+'/video/'+i.name)
    
            elif i.suffix.lower() in ('.zip', '.gz', '.tar'):
                move(i,begin+'/archives/'+i.name)

            else:
                move(i,begin+'/other/'+i.name)
        if not i.is_file():
            if i.name not in ('images' ,'documents','audio','archives','other'):
                sort(begin,i)
