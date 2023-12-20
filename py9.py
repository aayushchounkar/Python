#append means to add at the end
x=[1,2,3]
print(x)
y=x
print(y)
x[1]=15
print(x)

print(y)
x.append(12)
print(x)
print(y)

z=x.append(15)
print(z==None)
print(z)
print (y)
print(x)

x=x+[9,10]
print(x)
y=x
print(y)