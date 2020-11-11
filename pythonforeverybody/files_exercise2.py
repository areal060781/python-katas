from config import basedir

file = input('Enter a file name: ')
filename = basedir.joinpath('..', 'static', file)

try:
    handle = open(filename.absolute())
except:
    print('File cannot be opened:', file)
    exit()

count = 0
sum = 0
for line in handle:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        cpos = line.find(':')
        number = float(line[cpos+1:])
        sum += number
        count += 1

print('Average spam confidence:', str(sum))

