def save_credentials_users(path, users_info):
    with open(path, 'wb') as fh:
        for key,value in users_info.items():
            str_files=key+':'+value+'\n'
            str_bytes=str_files.encode()
            fh.write(str_bytes)
    return path
save_credentials_users("/Users/olha/Documents/GitHub/modul6/test6_10.txt",{'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'})