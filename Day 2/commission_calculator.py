# Start
print("\tHello and welcome to the commission calculator!")

# Var
name = input("First things first, enter your name: ")
sales = float(input("And how much has been the total sales this month?: $"))
commissions = round(sales * 13 / 100, 2)

# Output
print(f"\nPerfect, {name}! Based on your sales, you've earned a ${commissions} commission. Congratulations!")
