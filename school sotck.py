items = ["pencil", "eraser", "notebook", "sharpener", "scale"]
stock_counts = [12, 1, 8, 4, 3]



inventory = {item: count for item, count in zip(items, stock_counts)}
print("Full Inventory:", inventory)


in_stock_items = [item for item in items if inventory[item] > 0]
print("items in stock:", in_stock_items) 


chosen_item = input("Which item do you want to buy? ")


if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item, "is out of stock! Stopping the checker.")
    exit()


    prices = [10, 5, 40, 15, 20]
    markup = int(input("Enter the markup amount to add to every prices: "))


    marked_up_prices = list(map(lambda p: p + markup, prices))
    print("Marked Up prices:", marked_up_prices)


    item_index = items.index(chosen_item)
    chosen_price = marked_up_prices[item_prices]
    print("Price of", chosen_item, "after markup:", chosen_price)


    inventory[chosen_item] = inventory[chosen_item] - 1
    print(chosen_item, "purchased! Remaining stock:", inventory[chosen_item])

    print("")
    print("===== school store inventory checker =====")
    print("Item Bought:", chosen_item)
    print("Price Paid:", chosen_price)
    print("Updated Inventory:", inventory)
    print("================================================")