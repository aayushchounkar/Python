# def my_functon():
#     print("Hello rowdies ")

# my_functon()
# # print(type(my_functon))

# def ops():
#     if Choice==1:
#      print("the sum is =",a+b)

#     elif Choice==2:
#       print("the subs is =",a-b) 
    
#     elif Choice==3:
#       print("the multiplication  is =",a*b)
    
#     elif Choice==4:
#      print("the division is =",a/b)
#     else:
#       print("choose corrector opretor")
# print("1.addition")
# print("2.substraction")
# print("3.multiplication")
# print("4.division")
# Choice=int(input("Enter choice"))
# a=int(input("Enter a number "))
# b=int(input("Enter a number "))
# ops()




# There are two types of arguments:
# # 1.Positional arguments - No order flexibility
# def newfun(age,name):
#     print('Your name is:',name)
#     print('Your age is: ',age)
# newfun(18,'sahil')
# # 2.Keyword based Arguments - Flexibility of order
# def newfun(age,name):
#     print('Your name is:',name)
#     print('Your age is: ',age)
# newfun(name='Sahil',age=18)

#args(*)
# def my_function(*kids):
#   print("The child is ",(kids[2]))

# my_function("Emil", "Tobias", "Linus")


# def my_fun(*arss):
#   for i in arss:
#     print(i)
# my_fun(2)
# my_fun(3,4,5)
# my_fun(6,7,8,9)


# def my_func(a):
#     print(a)

# my_func(5*3+9)
# my_func(5*4+9)
# my_func(5*8+9)
# my_func(5*3+7)

#taking numbers and adding using tupple (listing it in tuple)
# def add(*args):
#     sum1=sum(args)
#     return sum1


# l=int(input("Enter number of arguements: "))
# my_list=[]
# for i in range(l):
#     my_list.append(int(input(f"Enter value: ")))
    
# print(add(*my_list))   

# #second method
# def addn(*ash):
#     sum=0
#     for i in ash:
#         for i in lts:
#             sum=sum+i
#     print('The sum of the elements is',sum)

# n=int(input('Enter the number of numbers you want to add: '))
# lts=[]
# for j in range(n):
#     num=int(input('Enter number: '))
#     lts.append(num)
# addn(lts)


#ARGS KWARGS TOGETHER
# def my_ash(*args,**kwargs):
#     print(args)
#     print(kwargs)
# my_ash("hello",1999,name="ASH",age=18,college="ITM UNIVERSITY")

#KEYVALUE PRINT SINGLE  
# def myfun(*args,**kwargs):
#     for key,value in kwargs.items():
#         print(key, '=', value)
#     for i in args:
#         print(i)

# myfun('hello','wassup',name='sahil',age=18,college='ITM')


# def namefun(*args):
#     for i in args:
#         print('Welcome',i, 'to ITM!') 
# name=str(input('What is your name?'))
# namefun(name)



# def namefun(**kwargs):
#     for key,value in kwargs.items():
#         print('Welcome',value, 'to ITM!') 
# n=str(input('What is your name?'))
# namefun(name = n)



# def fun():
#     name = input("Enter your name:")
#     print("Welcome",name,"to ITM\nEnter your details")
# # fun()
# def details(**kwargs):
#     details={}
#     for x in kwargs:
#         y=input(f"Enter your {x}: ")
#         details[x]=y
#     return details
# info=details(name="Name", age="Age", email="Email")
# print("Student Details:")
# for x, y in info.items():
#    print(f"{x}: {y}")



def namefun(**kwargs):
    for key, value in kwargs.items():
        print('Welcome', value, 'to ITM!')
        print(key, '=', value)
    # for value in kwargs.values:
    #     print(f"Name : {kwargs.get('Name')}")
    #     print(f"Email : {kwargs.get('Email')}")
    #     print(f"Number : {kwargs.get('Phone Number')}")


details = {}
choice = input('Would you like to enter a name? ')
count = 0
if choice.lower() == 'yes':
    name = input('What is your name? ')
    details['Name']=name
    # namefun(name=name)
if count == 0:
    choice = input('Would you like to enter an email? ')
    if choice.lower() == 'yes':
        email = input('What is your email? ')
        details['Email']=email
        # namefun(mail=email)
    elif choice.lower()=='no':
        pass
if count==0:
    number = input('What is your phone number? ')
    details['Phone Number']=number
    # namefun(number=number)


print("\nFull Details:")
for key, value in details.items():
    print(f"{key} = {value}")