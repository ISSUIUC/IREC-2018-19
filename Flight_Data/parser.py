input_filehandle = open('DATALOG.txt')

filecounter = 1

print(input_filehandle.readline())
print(input_filehandle.readline())

for line in input_filehandle.readlines():
    if filecounter != 1 and line == '':
        pass
