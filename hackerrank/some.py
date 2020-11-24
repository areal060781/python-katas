a = 'Margarita'

a_list = list(a)
n_list = list()

for i in range(len(a) - 1, -1, -1):
    n_list.append(a[i])

print(''.join(n_list))

# for v in a_list:
#     print(v)

# for i, v in enumerate(a_list):
#     print(i, v)
