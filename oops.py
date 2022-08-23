# class myclass:
#     x=5
# print(myclass)
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is "+self.name)
        # print("my age is "+str(self.age))
        # print(f"MY age is {self.age}")

obj=person("binu",21)
obj.myfunc()