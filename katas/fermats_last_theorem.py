'''Exercise 5.3. Fermat’s Last Theorem says that there are no positive integers a, b, and c such that

a n + b n = c n

for any values of n greater than 2.

1. Write a function named check_fermat that takes four parameters— a , b , c and n —and that checks to see if Fermat’s
theorem holds. If n is greater than 2 and it turns out to be true that
a n + b n = c n
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
print, “No, that doesn’t work.”

2. Write a function that prompts the user to input values for a , b , c and n , converts them to
integers, and uses check_fermat to check whether they violate Fermat’s theorem.'''


def check_fermat(a, b, c, n):
    result_expected = c**n
    theorem = a**n + b**n

    if n > 2 and theorem == result_expected:
        print("Holy smokes, Fermat was wrong! %d %d" % (theorem, result_expected))
    else:
        print("No, that doesn’t work. %d %d" % (theorem, result_expected))


a = int(input('Type a value for a: '))
b = int(input('Type a value for b: '))
c = int(input('Type a value for c: '))
n = int(input('Type a value for n: '))
check_fermat(a, b, c, n)

'''ccording to Fermat’s Last Theorem, no three positive integers a, b, c satisfy the equation, a^n + b^n = c^n for any 
integer value of n greater than 2. For n = 1 and n = 2, the equation have infinitely many solutions.
https://www.geeksforgeeks.org/fermats-last-theorem/'''
def testSomeNumbers(limit, n) :

    # if (n < 3):
    #     return

    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            # Check if there exists a triplet
            # such that a^n + b^n = c^n
            pow_sum = pow(a, n) + pow(b, n)
            c = pow(pow_sum, 1.0 / n)
            c_pow = pow(int(c), n)

            if (c_pow == pow_sum):
                print("Count example found %d %d %d" % (a, b, c))
                #return
    print("No counter example within given range and data")

# Driver code
testSomeNumbers(20, 3)