def get_recipe(path, search_id):
    with open(path, 'r') as fh:
        while True:
            line = fh.readline()
            if not line:
                break
            l = line.strip().split(',')
            if search_id == l[0]:
                record={"id": l[0], "name": l[1], "ingredients": l[2:]}
                return record
        return None
        
print(get_recipe("/Users/olha/Documents/GitHub/modul6/test6_6.txt", "60b90c2e13067a15887e1ae3"))