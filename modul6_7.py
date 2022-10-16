
def sanitize_file(source, output):
    with open(source,'r') as fh:
        line = fh.readline()
        for char in line:            
            if char in '0123456789':
                line = line.replace(char, '')
    with open(output,'w') as lh:
        lh.write(line)
    return output
print(sanitize_file("/Users/olha/Documents/GitHub/modul6/test6_7.txt","/Users/olha/Documents/GitHub/modul6/test6_7_1.txt"))
