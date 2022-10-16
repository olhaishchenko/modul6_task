def save_applicant_data(source, output):

    with open(output,'w') as oh:
        for i in range(len(source)):
            str_file = ''
            for key in source[i].keys():
                str_file += str(source[i][key])+','
            str_file = str_file.rstrip(',')+'\n'
            # if i == len(source)-1:
            #     str_file = str_file.rstrip('\n')
            oh.write(str_file)
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