file = input('Enter a file name: ')

if file == 'na na boo boo':
    print(file.upper() + " - You have been punk'd!")
    exit()

try:
    handle = open(file)
except:
    print('File cannot be opened: ', file)
    exit()

count = 0
for line in handle:
    count += 1

print('There were %d subject lines in %s' % (count, file))
