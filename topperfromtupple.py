topper_data = []

# Get user input for up to 3 students
for i in range(3):
    name = input(f"Enter the name of student {i + 1}: ")
    marks = []
    
    # Get marks for each subject
    for subject in range(4):
        mark = int(input(f"Enter the marks for subject {subject + 1} for {name}: "))
        marks.append(mark)
    
    # Add the student data to the list
    topper_data.append((name, *marks))

# Initialize variables to store information about the topper
max_marks = 0
topper_index = 0

# Iterate through the data
for i, student in enumerate(topper_data):
    _, marks = student[0], student[1:]

    # Calculate the total marks for each student
    total_marks = sum(marks)

    # Check if the current student has more marks than the current topper
    if total_marks > max_marks:
        max_marks = total_marks
        topper_index = i

# Print the name of the topper and their marks
print("\nTopper:", topper_data[topper_index][0])
print("Marks in Four Subjects:", topper_data[topper_index][1:])