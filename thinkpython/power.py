def is_power(a, b):
    # The only power of 1 is 1 itself
    if (b == 1):
        return (a == 1)

        # Repeatedly compute
    # power of b
    pow = 1
    while (pow < a):
        #print("%d * %d" % (pow, b), end="=")
        pow = pow * b
        #print(pow)

        # Check if power of b
    # becomes a
    return (pow == a)


print(is_power(1, 10))
print(is_power(1000, 10))
print(is_power(128, 2))
print(is_power(729, 3))
print(is_power(32, 2))
print(is_power(81, 3))
print(is_power(625, 5))
print(is_power(32, 4))
print(is_power(2, 1))
print(is_power(1, 1))
print("")

def is_power2(a, b):
    if a == b:
        return True

    if b == 1:
        return True

    if a % b == 0:
        return is_power2(a / b, b)
    else:
        return False


print(is_power2(10, 1))
print(is_power2(1000, 10))
print(is_power2(128, 2))
print(is_power2(729, 3))
print(is_power2(32, 2))
print(is_power2(81, 3))
print(is_power2(625, 5))
print(is_power2(32, 4))
print(is_power2(2, 1))
print(is_power2(1, 1))


