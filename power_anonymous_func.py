terms=10
result=list(map(lambda  x:2 **x,range(terms)))
print(f"The total terms are: {terms}" )
for i in range(terms):
    print(f"2 raised to power {i} is {result[i]}")