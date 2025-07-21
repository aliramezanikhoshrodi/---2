students = input("Enter the number of students: ")
new_students = int(students)
capacity = input("Enter the capacity of each seat: ")
new_capacity = int(capacity)
full_seat = new_students // new_capacity

print(f"{full_seat} seats will be completely filled.")