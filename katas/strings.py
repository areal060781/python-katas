string = 'X-DSPAM-Confidence:0.8475'
cpos = string.find(':')
number = float(string[cpos+1:])
print('%g' % number)

