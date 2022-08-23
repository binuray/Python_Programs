
# print(type(s))
# print(len(s))
# for x in s:
#     print(x)
# print("apple" in s)
# s.add("banana")
# print(s)
# s1={24,56,"kiwi"}
# s.update(s1)
# print(s)
# s.remove("orange")
# print(s)
# s.discard("apple")
# print(s)
# s.pop()
# print(s)
# s.clear()
# print(s)
# del(s)
# print(s)


s={"apple",23,45.67,"orange"}
print(s)
s1={23,56,78}
# s2=s.union(s1)
# print(s2)
# s.update(s1)
# print(s)
# s.intersection_update(s1)
# print(s)
# s.symmetric_difference_update(s1)
# print(s)
s2=s1.symmetric_difference(s)
print(s2)

