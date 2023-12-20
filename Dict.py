#key value pair
# dict are mutable
d={1:"hello","two":42,"blah":[1,2,3],55:{3:"rowdies",0:"saisir"}}
print(d)
print(d[1])
print(d["two"])
print(d["blah"])
print(d[55])
print(d[55][3])
del(d[55][0]) #deleting element of innerdict
print(d[55])