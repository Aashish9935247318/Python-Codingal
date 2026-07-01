def cube(number):
    return number*number*number



def by_there(number):
  if number %3 ==0:
    return cube(number)
  else:
     return False
  

print(by_there(9))
print(by_there(4))