#Calculating the projected saving for a user for a year.

monthly_income = int(input("Enter your monthly income: "))
total_expenses = int(input("Enter your monthly expenses: "))

savings = monthly_income - total_expenses

projected_savings = savings * 12 + (0.05 * savings *12)
print("Your monthly savings are", "$",savings,".")
print("Projected savings after one year, with interest, is:", "$",projected_savings,".")
