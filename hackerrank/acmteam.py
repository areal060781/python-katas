def acmTeam(topic):
    result = []
    total_members = len(topic) - 1

    x = 0
    counter = 1
    while x <= (total_members - 1):
        y = counter
        while y <= total_members:
            checks = bin(int(topic[x], 2) | int(topic[y], 2))
            result.append(checks[2:].count('1'))
            y += 1
        x += 1
        counter += 1

    print(max(result))
    print(result.count(max(result)))


acmTeam(['10101', '11100', '11010', '00101'])
# acmTeam(['10101', '11100', '11010'])
