# PART 1: Define a function with no arguments to greet the customer
def greet_customer():
    print("Welcome to the Art Supplies Store!")
    print("Get your colours, brushes, and paper here.")
 
# PART 2: Call the greet_customer function
greet_customer()
 
# PART 3: Ask for the price per item and the number of items bought
price_per_item = float(input("Enter the price per art item in dollars: "))
items_bought = int(input("Enter the number of art items bought: "))
 
# PART 4: Define a function that takes arguments and returns the total cost
def calculate_total(price, items):
    total = price * items
    return total
 
# PART 5: Call calculate_total and store the value it returns
total_cost = calculate_total(price_per_item, items_bought)
 
# PART 6: Use a built-in function to round the total, then print it
rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)
 
# PART 7: Ask how much money the customer paid
amount_paid = float(input("Enter the amount paid by the customer: "))
 
# PART 8: Define a function that takes arguments and returns the change due
def calculate_change(paid, total):
    change = paid - total
    return change
 

change_due = calculate_change(paid, total):
rounded_change = round(change_due, 2)


def thank_you_message(items):
    if items >= 5:
        return "Great choice! You picked many part art supplies for you project."
    else:
        return "Thanks for shopping at the art suppiles store!"

closing_message = thank_you_message(items_bought)



print("")
print("===== Art suppiles bill =====")
print("Price per item:", price_per_item)
print("Item bought:", items_bought)
print("Total cost:", total_cost)
print("Amount paid:", amount_paid)
print("Change due:", rounded_change)
print(closing_message)
print("================================")