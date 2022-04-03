num=900
num1=1000
print(f"Prime number between {num} and {num1} are :")
for num2 in range(num,num1+1):
    if num2>1:
        for i in range (2,num2):
            if (num2%i)==0:
                break
            else:
                print(num2)