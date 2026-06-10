String = input("Please enter your own String : ")

String2 = ('')

for i in String:
    String2 = i + String2

    print("\nThe Original String = ", String)
    print("The Reversed String = ", String2)