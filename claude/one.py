income = float(input("enter your monthly income: "))


num_expenses = int(input("How many expenses do you have: "))


expenses = []


for i in range(num_expenses):
    expense = float(input(f"enter expense #{i+1} : "))
    expenses.append(expense)

total_expenses = sum(expenses)
money_left = income - total_expenses


if money_left < 0:
    print(f"""Total expenses: {total_expenses}
              money left: {money_left}
              WARNING: you're overspending""")
elif money_left >= 500:
    print(f"""Total expenses: {total_expenses}
              money left: {money_left}
              You're doing GREAT!""")
else:
    print(f"""Total expenses: {total_expenses}
              money left: {money_left}
              You're managing okay""")


num_assignments = int(input("How many assignments do you have? "))

assignments = []

for i in range(num_assignments):
    grades = float(input(f"Enter your #{i+1} assignment grade: "))
    assignments.append(grades)

avg_grade = sum(assignments)/len(assignments)


print(f"\nYour average grade: {avg_grade:.2f}")


if 90 <= avg_grade <= 100:
    print("A (Excellent!)")
elif 80 <= avg_grade <= 89:
    print("B (Good job!)")
elif 70 <= avg_grade <= 79:
    print("C (Passing)")
elif 60 <= avg_grade <= 69:
    print("D (Needs improvement)")
else:
    print("F (Failed)")