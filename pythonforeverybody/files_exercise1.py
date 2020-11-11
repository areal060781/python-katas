from config import basedir

filename = basedir.joinpath('..', 'static', 'mbox-short.txt')

handle = open(filename.absolute())

for lines in handle:
    print(lines.upper())
