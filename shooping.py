valid = False

while not valid:
    try:

        bill_amount, discount_percent, people = input(
            "Enter bill amount, discount percent, and people separated by commas: "
        ).split(",")

        bill_amount = float(bill_amount)
        discount_percent = float(discount_percent)
        people = int(people)




        if bill_amount <= 0 or discount_percent < 0 or people < 0:
            raise ValueError


        discount_amount = bill_amount * discount_percent / 100
        final_amount = bill_amount - discount_amount


        amount_per_person = final_amount / people

    except Valueerror:
        print("Invalid input! Enter Value like this: 1000, 10, 2")

    except ZeroDivisionError:
        print("People cannot be 0. Please Enter at least 1 person.")

    else:
        print("
 ===== Shopping discount Summary =====")
         print("Original Bill:", bill_amount)
         print("discount_percent:", discount_percent)
         print("discount_amount:", discount amount)
         print("Final amount:", final_amount)
         print("Amount per person:", round(amount_per_person, 2))
         print("=====================================")
         valid = True

    finally:
        print("Discount check completed for this attempt

")