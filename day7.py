def motivate(name):
    print(f"You got this {name}, keep coding!")
user_name = input("what's your name? ")
motivate(user_name)

def multiply_numbers(a, b):
    return a * b
result = multiply_numbers(7, 9)
print(result)


def math_operations(a, b):
    if b == 0:
        division_result = "undefined (cannot divide by zero)"
    else:
        division_result = a / b
    return a + b, a - b, a * b, division_result


while True:
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))

    sum_result, difference_result, product_result, div_result = math_operations(a, b)

    choice = input("choose what u want (sum, diff, prod, div, exit, all): ").lower()

    if choice == "sum":
        print("sum:", sum_result)
    elif choice == "all":
        print(f"""1.sum: {sum_result}
                  2.diff: {difference_result}
                  3.prod: {product_result}
                  4.div: {div_result}""")
    elif choice == "diff":
        print("diff:", difference_result)
    elif choice == "prod":
        print("prod:", product_result)
    elif choice == "div":
        print("div:", div_result)
    elif choice == "exit":
        print("Thanks for trying our calculator!")
        break
    else:
        print("this option is not available")

    again = input("\nDo you want to try again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for trying our calculator!")
        break
