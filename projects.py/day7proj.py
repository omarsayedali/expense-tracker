def math_operations(a, b):
    if b == 0:
        division_result = "undefined (cannot divide by zero)"
        remainder_result = "undefined (cannot divide by zero)"
    else:
        division_result = a / b
        remainder_result = a % b

    exponent_result = a ** b
    return a + b, a - b, a * b, division_result, remainder_result, exponent_result


while True:
    print("\n⚙️  Welcome to the Advanced Calculator ⚙️")
    print("-" * 50)
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    sum_result, diff_result, prod_result, div_result, rem_result, exp_result = math_operations(a, b)

    print("\nChoose an operation:")
    print("1. sum ➕")
    print("2. diff ➖")
    print("3. prod ✖️")
    print("4. div ➗")
    print("5. remainder %️⃣")
    print("6. exponent ^")
    print("7. all 🔢")
    print("8. exit 🚪")

    choice = input("\n👉 Enter your choice: ").lower()

    print("\n" + "-" * 50)
    if choice in ["1", "sum"]:
        print("➕ Sum:", sum_result)
    elif choice in ["2", "diff"]:
        print("➖ Difference:", diff_result)
    elif choice in ["3", "prod"]:
        print("✖️ Product:", prod_result)
    elif choice in ["4", "div"]:
        print("➗ Division:", div_result)
    elif choice in ["5", "remainder", "%"]:
        print("🔹 Remainder:", rem_result)
    elif choice in ["6", "exponent", "^"]:
        print("⚡ Exponent:", exp_result)
    elif choice in ["7", "all"]:
        print(f"""🔢 Results:
1. Sum: {sum_result}
2. Difference: {diff_result}
3. Product: {prod_result}
4. Division: {div_result}
5. Remainder: {rem_result}
6. Exponent: {exp_result}""")
    elif choice in ["8", "exit"]:
        print("👋 Thanks for using our advanced calculator!")
        break
    else:
        print("⚠️ Invalid choice, please try again!")

    again = input("\nDo you want to try again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for using our advanced calculator!")
        break
