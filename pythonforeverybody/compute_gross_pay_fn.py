def computepay(hours, rate):
    extra_rate = 1.5
    journal = 40
    
    if (hours <= journal):
        pay = hours * rate
    else:
        pay = ((hours//journal*journal)*rate)+((hours-journal)*rate*extra_rate)
    
    return pay


hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

pay = computepay(hours, rate)
print('Pay: ' + str(pay))
