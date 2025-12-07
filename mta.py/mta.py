number = int(input("enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 5 == 0:
    print("Buzz")
elif number % 3 == 0:
    print("Fizz")
else:
    print(number)



name = input("Hello, Please enter your name: ")
age = int(input("How old are you? "))
print(f"Hello {name}, you're {age} years old")

num = int(input("enter the first number you want to add: "))
num2 = int(input("enter the sec number: "))
print(f"{num} + {num2} = {num + num2}")



user = input("Please enter the username: ")
if user.lower() == "admin":
    print("Access granted")
else:
    print("Access denied")



num3 = int(input("Please enter a number: "))
if num3 > 0:
    print("Positive")
elif num3 < 0:
    print("Negative")
elif num3 == 0:
    print("zero")
else:
    print("wrong input")



user_name = input("Please enter your username: ")
age = int(input("Please enter you age: "))
if user_name.lower() == "admin" and age >= 18:
    print("Access granted")
elif user_name.lower() == "admin" and age < 18:
    print("Admin access denied: too young")
else:
    print("Access denied")