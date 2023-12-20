
#program3
# str1=str(input("Enter a string-"))
# str2=str(input("Enter a string-"))
# uncommon_words=[]

# uncommon_words.extend(word for word in str1 if word not in str2)
# uncommon_words.extend(word for word in str2 if word not in str1)

# print(uncommon_words)




#program4
# def is_binary_string(input_string):
#     for char in input_string:
#         if char != '0' and char != '1':
#             return False
#     return True

# user_input = input("Enter a string: ")

# if is_binary_string(user_input):
#     print("The entered string is a binary string.")
# else:
#     print("The entered string is not a binary string.")


#************************************************************************
#program1
# print('Hello World')
# print("Hello World")
# print('''Hello World''')
# print("""Hello 
#       World
# """)

#program2
# str = "Hello World"
# print(str)
# print(str[0])
# print(str[1])
# print(str[-1])
# print(str[-2])
# print(str[0:5])
# print(str[2:-1])
# for char in str:
#     print(char,end=" ")
# print()

#program3
# str1 = input("String 1: ")
# str2 = input("String 2: ")
# uncommon_words = []
# uncommon_words.extend(word for word in str1 if word not in str2)
# uncommon_words.extend(word for word in str2 if word not in str1)
# print(uncommon_words)


#program4
# str = input("Enter binary string: ")
# flag = 1
# for char in str:
#     if char != "1" and char != "0":
#         flag = 0

# if flag ==1:
#     print("It is Binary")
# else:
#     print("Not binary")



#program5
# input_str = input("> ")
# char_frequency = {}

# for char in input_str:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1

# least_frequent_char = min(char_frequency, key=char_frequency.get)
# print("Least frequent character:", least_frequent_char)


# #program6
# str = input(">  enter a string= ")
# index = int(input("Index to remove: "))
# mod_str = str[:index] + str[index+1:]
# print(mod_str)



#program7
# class Employee:
    
#     def get_details(self):
#         self.name = input("Enter name: ")
#         self.id = input("Enter employee id: ")
#         self.gender = input("Enter gender: ")
#         self.city = input("Enter city: ")
#         self.salary = input("Enter salary: ")
#     def display_details(self):
#         print("*****DETAILS*****")
#         print("Name of employee=",self.name)
#         print("Id number=",self.id)
#         print("Gender=",self.gender)
#         print("City=",self.city)
#         print("Salary of employee=",self.salary)
# e1 = Employee()
# print("Employee Details:\n")
# e1.get_details()
# e1.display_details()



