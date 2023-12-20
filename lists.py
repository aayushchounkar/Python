# x=[1,"Hello",(3+2j)]
# print(x)
# print(x[2])
# print(x[0:2])


#append
x=[1,2,3]
y=x
x[1]=15
print (x)
print(y)
x.append(12)
print(x)
print(y)
y.append(8)
print(x)
print(y)
z=x.append(21)
z==None
print(x)
print(y)
print(z)