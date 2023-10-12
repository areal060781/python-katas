# Standard solution for Even numbers
def list_even_numbers_standard():
    n = int(input("Input integer number: "))
    even_numbers = []
    for i in range(1, n):
        if not i % 2:
            even_numbers.append(i)
    return even_numbers


def list_even_numbers_comprehension():
    n = int(input("Input integer number: "))
    even_numbers = [i for i in range(1, n) if not i % 2]

    return even_numbers
