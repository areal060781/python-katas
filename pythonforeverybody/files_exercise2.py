file = input('Enter a file name: ')

try:
    handle = open(file)
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

