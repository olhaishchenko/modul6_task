def total_salary(path):
    fh = open (path,'r')
    sum_salary = 0
    while True:
        line = fh.readline()
        if not line:
            break
        ind = line.rfind(',')
        salary = int(line[ind+1::])
        sum_salary +=salary
    fh.close()
    return float(sum_salary)
