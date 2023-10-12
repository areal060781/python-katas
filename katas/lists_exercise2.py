from config import basedir

filename = basedir.joinpath('..', 'static', 'mbox-short.txt')

fhand = open(filename.absolute())
count = 0
for line in fhand:
    line = line.rstrip()
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])