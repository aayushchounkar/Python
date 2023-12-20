d={1:'hello','two':42,'blah':[1,2,3]}
print(d)

print(d['blah'])
print(d[1])
print(d['two'])

print(d)
d['two']=99   #modify
print(d)

d[7]='new entry'#add
print(d)

d[2]='there'
print(d)

del(d[2])
print(d)
