def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    cost = meal_cost + tip + tax
    return round(cost)

# solve(12.0, 20, 8)
# solve(15.50, 15, 10)
# solve(10.25, 17, 5)