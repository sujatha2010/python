student_name = 'abc'

marks = {'abc':77, 'azv':55, 'mno': 87}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print("no entry found")
    