# num=float(input("Enter the number:"))
# if num>0:
#     print(f"{num} is positive")
# elif num==0:
#     print(f"{num} is equal to Zero")
# else:
#     print(f"{num} is negative")

#using nested if statement
num=float(input("Enter number to check:"))
if num>=0:
    if num==0:
        print(f"{num} is equal to zero")
    else:
        print(f"{num} is positive")
else:
    print(f"{num} is neagtive")