def is_triangle(a, b, c):
    sum_a_b = a + b
    sum_a_c = a + b
    sum_b_c = b + c

    if a > sum_b_c or b > sum_a_c or c > sum_a_b:
        print("No")
    else:
        print("Yes")
        if a == sum_b_c or b == sum_a_c or c == sum_a_b:
            print("A degenerate triangle")


a = int(input("Type a length for a: "))
b = int(input("Type a length for b: "))
c = int(input("Type a length for c: "))
is_triangle(a, b, c)

