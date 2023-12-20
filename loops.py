#sum=0
# for i in range (1,11):
#     sum=sum +i
#     print("the sum is",sum)
#num= int(input("Enter the number of rows : "))

# right angle tringle star design
# for i in range (1,num+1):

#     for j in range( 0 , i): 
#         print("*",end=" ")

#     print()
   
  #square
# for j in range (0,num):
#     for i in range (1,num+1):   
      
#         print ("*",end=" ")

#     print()


# lower right angle tringle star design
# for i in range (num,0,-1):
#     for j in range (0,i):  
#         print ("*",end=" ") 
#     print(" ")
    

 #arrow
# for i in range (1,num+1):

#     for j in range( 0 , i): 
#         print("*",end=" ")

#     print()

# for i in range (num-1,0,-1):
#     for j in range (0,i):  
#         print ("*",end=" ") 
#     print(" ")



# #left face arrow
# num= int(input("Enter the number of rows : "))
# for i in range (0,num+1):

#     for j in range(0, i): 
#         print("*",end=" ")

#     print()

# for i in range (num-1,0,-1):
#     for j in range (0,i):  
#         print ("*",end=" ") 
#     print(" ")



# # diamond star pattern
# n = int(input("enter a number"))

# # upward pyramid
# for i in range(n):
#     for j in range(n - i - 1):
#         print(' ', end='')
#     for j in range(2 * i + 1):
#         print('*', end='')
#     print()

# # downward pyramid
# for i in range(n - 1):
#     for j in range(i + 1):
#         print(' ', end='')
#     for j in range(2*(n - i - 1) - 1):
#         print('*', end='')
#     print()

# 

val=65
for i in range(0,5):
    for j in range (0,i+1):
        ch=chr(val)
        print (ch,end=" ")
    val=val+1
    print ()
