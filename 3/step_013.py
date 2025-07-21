students = input("Enter the number of students: ")
new_students = int(students)
capacity = input("Enter the capacity of each seat: ")
new_capacity = int(capacity)

lonely_students = new_students % new_capacity

print(f"{lonely_students} students were left alone.")