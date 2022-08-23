# f1=[23,45,67,89]
# f2=[12,21,43,65]
# for x in f1:
#     for y in f2:
#         print(x,y,end="")
# for x in range(5):
#     print("*")
#     for y in range(5):
#         print("*",end=" ")
for x in range(0,5):
    for y in range(x+1):
        print(x,end=" ")
    print("\r")


