import re

punctuations = ':;,.!?'
inp = 'you, shall not pass!'
match = re.search(r'([:;,.!?]+)$', inp)
print(match)
end_puncs = match.group(1) if match is not None else ''
print(end_puncs)
rev = ' '.join(reversed(re.findall('[\w:;,.!?]+', inp.rstrip(punctuations)))) + end_puncs
print(rev)
