def save_applicant_data(source, output):
   
    with open(output,'w') as oh:
        for i in range(len(source)):
            str_file = source[i]['name']+','+str(source[i]['specialty'])+','+str(source[i]['math'])+','+str(source[i]['lang'])+','+str(source[i]['eng'])+'\n'     
            oh.writelines(str_file)
    return output
print(save_applicant_data([
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
],"/Users/olha/Documents/GitHub/modul6/test6_8.txt"))