# x=lambda a,b:a+b
# print(x(20,30))
def func(a):
    print(a)
    return lambda n:n*a
sum=func(4)
print(sum(5))