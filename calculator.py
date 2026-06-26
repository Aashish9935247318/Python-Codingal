def add(P, Q):

    return P + Q 
def subtract(P, Q):

    return P - Q
def multiply(P, Q):

    return P * Q
def divide(P, Q):

    return P / Q


print ("Please select the operation.")
print ("a. Add")
print ("b. Subtract.")
print ("c. Multiply.")
print ("d. Divide")

choice = input("Please enter choice (a/ b/ c/ d/): ")

num_1 = int (input ("Please enter the first number: "))
num_2 = int (input ("Please enter the number second number: "))

if choice == 'a':
    print (num_1, " + ", num_2, " = ", Add(num_1, num_2))

elif choice == 'b':
    print (num_1, " - ", num_2, " = ", Subtract(num_1, num_2))

elif choice == 'c':
    print (num_1, " * ", num_2, " = ", Multiply(num_1, num_2))

elif choice == 'd':
    print (num_1, " / ", num_2, " = ", Divide(num_1, num_2))