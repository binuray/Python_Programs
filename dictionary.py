# mydict={
#     "dict1":{
#         "brand":"HP",
#         "RAM":4,
#         "Processor":"i3"
#
#     },
#     "dict2":{
#         "brand":"Dell",
#         "RAM":8
#     },
#     "dict3":{
#         "brand":"Lenovo",
#         "RAM":64
#     }
# }
# print(mydict["dict2"].values())
thisdict={
    "name":"binu",
    "rollno":23,
    "branch":"CS"
}
print(thisdict)
print(type(thisdict))
print(len(thisdict))
print(thisdict.keys())
print(thisdict.values())
thisdict["name"]="nikhil"
print(thisdict)
if "name" in thisdict:
    print("yes")
else:
    print("No")

thisdict.update({"year":2022})
print(thisdict)
thisdict.pop("rollno")