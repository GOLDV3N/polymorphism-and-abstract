'''Abstract Class
Outline:
Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this example.'''




from abc import ABC , abstractmethod
class  abs (ABC):
    def print(self,x):
        print("passed value",x)

    @abstractmethod
    def task(self):
        print("we are in a absc task")

class test_class(abs):
    def task(self):
        print("we are in test_class task")
test_obj = test_class()
test_obj.task()
test_obj.print(100)