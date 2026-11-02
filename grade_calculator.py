student_name = input("Enter student name: ")
math = int(input("Enter Math marks: "))
english = int(input("Enter English marks: "))
python = int(input("Enter Python marks: "))

# Validation: Check if marks are between 0 and 100
if (math < 0 or math > 100) or (english < 0 or english > 100) or (python < 0 or python > 100):
    print("Invalid marks! Marks must be between 0 and 100.")
else:
    # Average
    average = (math + english + python) / 3

    # Grade
    if average >= 80:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "A-"
    elif average >= 50:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    # Display results
    print(f"Student Name: {student_name}")
    print(f"Average Marks: {average:.2f}")
    print(f"Final Grade: {grade}")