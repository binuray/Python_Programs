# def fun(k):
#     if(k>0):
#         result=k+fun(k-1)
#         print(result)
#     else:
#         result=0
#     return result
# print("Recursion example")
# fun(4)
# x=lambda a,b:a+b
# print(x(7,4))
# def fun(n):
#     return lambda a:a*n
# myval=fun(2)
# print(myval(22))

# class person:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
# p1=person("binu",22)
# print(p1.name)
# print(p1.rollno)

# class person:
#     def __init__(myobject,name,age):
#         myobject.name=name
#         myobject.age=age
#     def fun(nothing):
#         print("hello"+nothing.name)
# p1=person("john",21)
# p1.fun()



# class person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# x=person("John","Doe")
# x.printname()
# class student(person):
#     def __init__(self,age,rollno):
#         self.age=age
#         self.rollno=rollno
#     def printname(self):
#         print(self.age,self.rollno)
# x=student(21,1)
# x.printname()

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def fun(self):
#         print(self.name,self.age)
# class stu(person):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#
# x=stu("binu",21)
# x.fun()

tup=("hello",22,"world")
obj=iter(tup)
print(next(obj))
print(next(obj))
print(next(obj))

































