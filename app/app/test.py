f = open('urls.py', 'r')

for line in f:
    if len(line.split(',')) == 4:
        print(line.split(',')[2].split("'")[1])
f.close()
