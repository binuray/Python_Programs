while(True):
    print("press q to quite")
    a=input("Enter a number")
    if a=='q':
        break
    try:
        a=int(a)
        if a>6:
            print("you entered a number greater than 6")
    except Exception as e:
        print(f"Your input resulted is an error{e}")
print("Thanks for playing")