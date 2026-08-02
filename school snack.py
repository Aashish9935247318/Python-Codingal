snack_box1 = {"chips", "juice", "cookies", "chocolates", "cold drink"}
snack_box2 = {"banana", "apple", "sandwich"}
print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)



snack_box1.add("banana")
print("Snack box 1 after adding chapati", snack_box1)


common_snacks = snack_box1.intersection(snack_box1)
print("Snacks in both boxes:", common_snacks)


import array as arr
snack_counts = arr.array('i', [4, 6, 3, 5,])
print("Snack counts array:", snack_counts)


snack_counts.insert(0, 2)
snack_counts.append(7)
print("Snacks counts after adding items:", snack_counts)


count_of_5 = snack_counts.counts.counts(5)
print("Number of times 5 appears:", count_of_5)


snack_counts.reverse()
print("Reversed snack count array:", snack_counts)


print("")
print("===== School Snack Counter =====")
print("Snack Box 1:", snack_box1)
print("snack box 2:", snack_box2)
print("Shared snacks",common_snacks)
print("Snack counts:", snack_counts)
print("================================")