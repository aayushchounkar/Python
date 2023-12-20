#strings are immutable
#deletaion of chars and replace of char is not allowed 
#a="ITM SKILLS UNIVERSITY"
# for letter in str(a):
#     print(letter)



# print(a[-21:-1])
# #print(a[-21: :-1])
# print(a[:])

# a="kharghar"
# del (a)
# print (a)

# a="kharghar"
# print(a[2:5])
#index = 0
# while index < len(my_string):
#     print(my_string[index])
#     index += 1

def checkOccurence(str,ch,choice):
    if choice==1:
        if ch in str:
            return str.index(ch)
        else:
            return -1
    elif choice==2:
        index = 0
        for i in range(len(str)):
            if str[i] == ch:
                index = i
                return index
        
        return -1
    

str = input("Enter string: ")
choice = int(input("1)String\n2)Char\nEnter choice: "))

if choice==1:
    char = input("Enter substring to find for: ")
    index = checkOccurence(str,char,choice)
    if index==-1:
        print(f"'{char}' not found in string '{str}'")
    else:
        print(f"'{char}' found from position {index} in '{str}'")
elif choice==2:
    count = 0
    char = input("Enter character to find for: ")
    index = checkOccurence(str,char,choice)
    for i in range(len(str)):
        if str[i]==char:
            count+=1
    if index==-1:
        print(f"'{char}' not found in string '{str}'")
    else:
        print(f"'{char}' found at position {index} in '{str}', total of {count} times in string")