def computegrade(score):
    if (not(score >= 0.0 and score <= 1.0)):
        grade = 'Bad score'
    elif (score >= 0.9):
        grade = 'A'
    elif(score >= 0.8):
        grade = 'B'
    elif(score >= 0.7):
        grade = 'C'
    elif(score >= 0.6):
        grade = 'D'
    else:
        grade = 'F'

    return grade

try:
    score = float(input('Enter a score: '))
    print(computegrade(score))
except:
    print('Bad score')
