f = open('grade.txt', 'r')
newFile = open('pass.text', 'w')
failFile = open('fail.text', 'w')

#count = 1

for check in f:
    checkline = check.split()
    # print(checkline)
    if checkline[2] == 'P':
        newFile.write(check)
    else:
        failFile.write(check)

f.close()
newFile.close()
failFile.close()



#p = open('grade.txt', 'a')

#p.write('Frank 30 P''\n')

#print(p)



'''

#print(str(count) + " " + n)
    #count = count + 1

for n in f:
    if n == 'P':
        print(n )
# print(f.read())
'''