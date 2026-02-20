# Program to calculate total cost of 3 items
# Apply 10% discount if total cost is greater than $50

# Taking input for three item prices
price1 = float(input("Enter price of item 1: $"))
price2 = float(input("Enter price of item 2: $"))
price3 = float(input("Enter price of item 3: $"))

# Calculating original total
original_total = price1 + price2 + price3

# Initialize discount
discount = 0

# Apply 10% discount if total is greater than 50
if original_total > 50:
    discount = original_total * 0.10  # 10% discount

# Calculate final amount after discount
final_amount = original_total - discount

# Display results
print("\n----- Bill Details -----")
print("Original Total: $", original_total)
print("Discount: $", discount)
print("Final Amount: $", final_amount)
