
print("================================")
print("     STUDENT GRADE CALCULATOR")
print("================================")

name = input("Enter Student Name: ")

subjects = ["Tamil", "English", "Maths", "Science", "Computer"]

marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input("Enter " + subject + " Mark: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

total = sum(marks)
average = total / len(subjects)

if any(mark < 35 for mark in marks):
    grade = "F"
    result = "FAIL"
elif average >= 90:
    grade = "A+"
    result = "PASS"
elif average >= 80:
    grade = "A"
    result = "PASS"
elif average >= 70:
    grade = "B"
    result = "PASS"
elif average >= 60:
    grade = "C"
    result = "PASS"
else:
    grade = "D"
    result = "PASS"

print("\n========== STUDENT RESULT ==========")
print("Student Name:", name)

for subject, mark in zip(subjects, marks):
    print(subject + ":", mark)

print("------------------------------------")
print("Total Marks:", total, "/ 500")
print("Average:", round(average, 2))
print("Grade:", grade)
print("Result:", result)
print("====================================")
