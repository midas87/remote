count = []

while True:
    numb = input('Enter a number: ')
    if numb.isnumeric():
        count.append(numb)
    if numb == 'done':
        break
#print(len(count))

for i in range(0, len(count)):
    count[i] = int(count[i])
print(sum(count), len(count), )

#print(int(count[i]))
