 #Count the number of words
str = input("Enter a sentence: ")

count = 1
if str == "":
    print("Empty string. Words = 0")
    exit()

for char in str:
    if char==" ":
        count+=1
    
print(f"Number of words: {count}")