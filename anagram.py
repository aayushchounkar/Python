str1=input("Enter string 1 ")
str2=input("Enter string 2 ")

for i in str1:
    if i in str2:
        continue
    else:
        print("not an anagram")
        exit()

print ("it is an anagram")