from abc import ABC, abstractclassmethod

class Abcclass(Abc):


    def print(self,x):
        print("Passed value: ", x)


    @abstractclassmethod
    def task(self):
        print("We are inside Abclass task")

class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)