# Fibonacci numbers module
# the sum of two elements defines the next

def fib(n):
    "write Fibonacci series up to n"
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


def fib2(n):
    """return Fibonacci series up to n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def standard_fibo(n):
    n_fib = None

    if n < 1:  # check that input is a valid
        print('N must be > 0')
    elif n == 1:  # first Fib number is 0
        n_fib = 0
    elif n == 2:  # second number - 1
        n_fib = 1
    else:
        prev_2, prev_1 = 0, 1  # prev_2 – N-2 element, prev_1 – N-1
        for i in range(2, n):
            n_fib = prev_2 + prev_1  # calculate a next value of the Fib
            prev_2 = prev_1  # shift prev_2 and prev_1 values
            prev_1 = n_fib
    return n_fib


def recursive_fibo(n):
    """Get a Nth element of the Fibonacci sequence."""
    if n == 1:  # base case
        value = 0
    elif n == 2:  # base case
        value = 1
    else:
        value = recursive_fibo(n - 2) + recursive_fibo(n - 1)  # recursive call

    return value
