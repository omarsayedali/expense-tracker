numbers = []
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))
num4 = int(input("enter the forth number: "))
num5 = int(input("enter the fifth number: "))
numbers.append(num1)
numbers.append(num2)
numbers.append(num3)
numbers.append(num4)
numbers.append(num5)
for i, number in enumerate(numbers, start=1):
    print(f"{i}. {number}")
print(max(numbers))
print(min(numbers))
print(sum(numbers))


numbers = []

for i in range(1, 6):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

print("\n📋 Your numbers:")
for i, number in enumerate(numbers, start=1):
    print(f"{i}. {number}")

print(f"\n✅ Highest number: {max(numbers)}")
print(f"⬇️ Lowest number: {min(numbers)}")
print(f"➕ Sum of numbers: {sum(numbers)}")




students = {}

while True:
    print("""
What do you want to do:
1. Add student and their grade
2. Remove student
3. Show all students
4. Exit
""")

    try:
        option = int(input("Choose an option (1/2/3/4): "))
    except ValueError:
        print("❌ Please enter a valid number (1-4).")
        continue

    if option == 1:
        try:
            count = int(input("How many students do you want to add? "))
            for i in range(count):
                name = input("Enter student name: ")
                grade = int(input(f"Enter {name}'s grade: "))
                students[name] = grade
            print("✅ Students added successfully!")
        except ValueError:
            print("❌ Invalid input, please enter numbers only for grades.")

    elif option == 2:
        name = input("Enter the name of the student you want to remove: ")
        if name in students:
            del students[name]
            print(f"🗑️ {name} has been removed successfully.")
        else:
            print("⚠️ Student not found!")

    elif option == 3:
        if students:
            print("\n📋 Current Students:")
            for i, (name, grade) in enumerate(students.items(), start=1):
                print(f"{i}. {name}: {grade}")
        else:
            print("😢 No students added yet!")

    elif option == 4:
        print("👋 Goodbye, have a great day!")
        break

    else:
        print("❌ Invalid choice, try again.")

