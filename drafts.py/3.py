print("Hello, welcome to the student tracker")
students = {}
while True:
        try:     
             studnents_names = int(input("how many students do you want to add: "))
             for i in range(studnents_names):
                    name = input("What's the student's name: ")
                    grade = int(input(f"enter {name}'s grade: "))
                    students[name] = grade
                    print("student added successfully")
        except ValueError:
               print("Invalid input, please enter numbers only for grades")

               print("\n📋 Current Students:")
        for i, (name, grade) in enumerate(students.items(), start=1):
                print(f"{i}. {name}: {grade}")

        avg = sum(students.values()) / len(students)
        print(f"\n📊 Average grade: {avg:.2f}")
        print(f"🏆 Top student: {max(students, key=students.get)} ({max(students.values())})")
        print(f"lowest student: {min(students, key=students.get)} ({min(students.values())})")

        print(f"{50*"-"}thanks for using our student tracker{50*"-"}")
        break




