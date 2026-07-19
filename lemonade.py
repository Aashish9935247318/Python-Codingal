def greet_customer():
    print("Welcome to the Lemonade Stand!")
    print("Fresh lemonade, made just for you.")


    greet_customer()


    price_per_cup = float(input("Enter the price per cup in dollers: "))
    cup_sold = int(input("Enter the number of cups sold: "))

    def calculate_total(price, cups):
        total = price * cups
        return total
    
    total_cost = calculate_total(price_per_cup, cup_sold)





    rounded_total = round(total_cost, 2)
    print("Total Cost:", rounded_total)





    def calculate_change(paid, total):
        change = paid - total 
        return change 
    

    change_due = calculate_change(Amount_paid, rounded_total)
    rounded_change = round(change_due, 2)



    def thank_you_message(cups):
        if cups >= 5:
            return "Wow, big order! Thank You so much for you support!"
        else:
            return "Thanks for stopping by the stand!"

            closing_message = thank_you_message(cups_sold)


            print("")
            print("==== LEMONADE STAND RECEPT =====")
            print("price per cup:", price_per_cup)
            print("cup_sold:", cup_sold)
            print("total cost:", rounded_total)
            print("Amount paid:", amount_paid)
            print("Change due:", rounded_change)
            print(closing_message)
            print("=================================")