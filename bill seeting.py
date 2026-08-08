def total_bill(bill_amount, tip_perc):

    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")
    return total





    total_bill(150, 20)



    def seeting_arrangements(guests):
        '''This is a recursive function to find the number of seeting arrangements for guests'''


        if guests == 0 or guests == 1:
            return 1


        else:
            ruturn guest * seeting_arrangements(guests - 1)


    print(seeting_arrangements._doc_)



    print("Seeting arrangements for 1 guest:", seeting_arrangements(1))
    print("Seeting arrangements for 2 guest:", seeting_arrangements(2))
    print("Seeting arrangements for 3 guest:", seeting_arrangements(3))
    print("Seeting arrangements for 4 guest:", seeting_arrangements(4))