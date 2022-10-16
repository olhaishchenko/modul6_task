from locale import normalize
from os import remove
from pathlib import Path
from shutil import move
begin = "/Users/olha/Downloads"
p = Path(begin)
# Path(begin+'/images').mkdir()  
# Path(begin+'/documents').mkdir()
# Path(begin+'/audio').mkdir()
# Path(begin+'/video').mkdir()
# Path(begin+'/archives').mkdir()
# Path(begin+'/other').mkdir()


def ordnung(begin):
    for i in p.iterdir():
        if i.is_file():
            if i.suffix.lower() in ('.jpeg', '.png', '.jpg', '.svg'):
                # print(i) 
                # print(i.name)
                move(i,Path(begin+'/images/'+i.name))
                # print(Path(begin+'/images/'+i.name))

            if i.suffix.lower() in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'):
                move(i,Path(begin+'/documents/'+i.name))

            if i.suffix.lower() in ('.mp3', '.ogg', '.wav', '.amr'):
                move(i,Path(begin+'/audio/'+i.name))

            if i.suffix.lower() in ('.avi', '.mp4', '.mov', '.mkv'):
                move(i,begin+'/video/'+i.name)
    
            if i.suffix.lower in ('.zip', '.gz', '.tar'):
                move(i,begin+'/archives/'+i.name)

            else:
                move(i,begin+'/other/'+i.name)
  
        # elif i in ('images' ,'documents','audio','archives','other'):
        #     break
        # else: 
        #     # перевірити на пустоту і видалити????
        #     ordnung(i)
ordnung(begin)