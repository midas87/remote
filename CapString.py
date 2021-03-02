fileHand = input('Enter a file name: ')
try:
    f = open(fileHand)
except FileNotFoundError:
    print('file not found',fileHand)
    quit()

print(f.read().upper())
