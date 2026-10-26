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