from config import basedir

filename = basedir.joinpath('..', 'static', 'mbox-short.txt')
fhand = open(filename.absolute())
count = 0

for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 or words[0] != 'From': continue
    print(words[1])

    count += 1

print('There were %d lines in the file with From as the first word' % count)