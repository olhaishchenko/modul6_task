import shutil


def create_backup(path, file_name, employee_residence):
    with open(path+file_name,'wb') as fh:
    # with open(path+'/'+file_name,'wb') as fh:
        for key,value in employee_residence.items():
            string = key + ' ' + value + '\n'
            string_bytes = string.encode()
            fh.write(string_bytes)
#     return path+file_name

# create_backup("/Users/olha/Documents/GitHub/modul6/", 'test6_13.txt', {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'})    
        
            
    archive_name = shutil.make_archive('backup_folder', 'zip', path)
    return archive_name