total = 0
count = 0
average = 0
while True:
    value = input('Enter a number:  ')

    if value == 'done':
        break

    try:
         number = int(value)

         total += number
         count += 1
         average = total / count
    except (ValueError):
        print('Invalid input')
        continue


print(str(total) + ' ' + str(count) + ' ' + str(average))

