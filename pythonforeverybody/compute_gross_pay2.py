hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
extra_rate = 1.5
journal = 40

#print(type(hours))
#print(type(rate))


if (hours <= journal):
    pay = hours * rate
else:
    pay = ((hours//journal*journal)*rate)+((hours-journal)*rate*extra_rate)


print('Pay: ' + str(pay))
