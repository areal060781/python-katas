try:
    score = float(input('Enter a score: '))

    if (not(score >= 0.0 and score <= 1.0)):
        print('Bad score')
    elif (score >= 0.9):
        print('A')
    elif(score >= 0.8):
        print('B')
    elif(score >= 0.7):
        print('C')
    elif(score >= 0.6):
       print('D')
    else:
       print('F')
except:
    print('Bad score')
