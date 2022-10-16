def get_credentials_users(path):
    path_list = []
    with open(path, 'rb') as fh:
        new_str = fh.read().decode()
        new_str = new_str.replace('\n', ',')
        path_list = new_str.split(',')
    return path_list


get_credentials_users("/Users/olha/Documents/GitHub/modul6/test6_10.txt")
    
   