child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
drink_cost = float(input("What is the cost of a drink? "))
appetizer_cost = float(input("What is the cost of an appetizer? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))
number_of_drinks = int(input("How many drinks? "))
number_of_appetizers = int(input("How many appetizers? "))
tax_rate = float(input("What is the sales tax rate? "))
tip_percentage = float(input("What is the tip percentage? "))

print()

subtotal = (child_price * number_of_children) + (adult_price * number_of_adults) + (drink_cost * number_of_drinks) + (appetizer_cost * number_of_appetizers)
print(f"Subtotal: ${subtotal:.2f}" )

sales_tax = (subtotal * tax_rate) / 100
print(f"Sales tax: ${sales_tax:.2f}")

tip_amount = (subtotal * tip_percentage) / 100
print(f"Tip: ${tip_amount:.2f}")

total = subtotal + sales_tax + tip_amount
print(f"Total: ${total:.2f}")

print()

payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total
print(f"Change: ${change:.2f}")