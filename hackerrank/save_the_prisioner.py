# https://www.hackerrank.com/challenges/save-the-prisoner/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def save_the_prisoner(n, m, s):
    return ((s - 1 + m - 1) % n) + 1