def read_employees_from_file(path):
    fh = open(path,'r')
    str_new = fh.read()
    str_new = str_new.rstrip('\n')
    a = str_new.split('\n')
    fh.close()
    return a

print(read_employees_from_file("/Users/olha/Documents/GitHub/modul6/test.txt"))