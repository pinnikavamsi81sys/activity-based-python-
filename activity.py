
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))
    subject = float(input("Enter minimum subject score: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family income: "))

    if marks >= 75 and subject >= 60 and attendance >= 75 and income <= 200000:
        students.append([name, marks, attendance, income])
        print("Eligible for scholarship")
    else:
        print("Not eligible for scholarship")

# Rank students by marks, then attendance
students.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("\n--- Scholarship Ranking ---")

if len(students) == 0:
    print("No eligible students")
else:
    rank = 1
    for s in students:
        print(rank, s[0], "- Marks:", s[1],
              "Attendance:", s[2])
        rank += 1

