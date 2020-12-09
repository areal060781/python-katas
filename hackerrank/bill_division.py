# https://www.hackerrank.com/challenges/bon-appetit/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def bonappetit(bill, k, b):
    new_bill = (sum(bill) - bill[k]) / 2

    return "Bon Appetit" if b == new_bill else int(b - new_bill)

