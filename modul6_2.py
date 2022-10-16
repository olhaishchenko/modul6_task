def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    str=''
    for items in employee_list:
        for item in items:
            str += item+'\n'
    str=str.rstrip('\n')
    fh.write(str)
    fh.close()
    return path


# a = [[4, 5, 6], [7, 8], [6]]
b=[['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

write_employees_to_file(b,"/Users/olha/Documents/GitHub/modul6/test.txt")
# for items in b:
#     for item in items:
#         print(item)