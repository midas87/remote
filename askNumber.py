count = []
res = " "

while True:
    numb = input('Enter a number: ')
    if numb.isnumeric():
        count.append(numb)
    if numb == 'done':
        break
    try:
        if res in numb or numb.isalpha():
            print('Invalid input, Please enter numbers only')
    except NameError:
        print('try again')
for i in range(0, len(count)):
    count[i] = int(count[i])
print(sum(count), len(count), sum(count)/len(count))
