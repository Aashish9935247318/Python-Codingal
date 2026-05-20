print("Enter Marks Obtained in 4 subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))
physics = int(input("physics :"))

sum = math+english+science+hindi+physics
print("sum of math,english,science,hindi and physics = ",sum)

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)