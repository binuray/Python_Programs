def print_factors(x):
    print(f"The factors of {x} are:")
    for i in range(1,x+1):
        if x%i==0:
            print(i)
num=int(input("Enter Number"))
print_factors(num)