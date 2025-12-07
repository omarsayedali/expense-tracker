def grade_students(grade):
   if grade >= 90:
        return "A"
   elif grade >= 80:
        return "B"
   elif grade >= 70:
        return "C"
   elif grade >=60:
        return "D"
   else:
        return "F"
    
while True:
    name = input("please enter your name: ").capitalize()
    try:
        grade = int(input("please enter your grade:(0-100) "))
    except ValueError:
        print("❌ invalid input, please enter a number.")
        continue
    
    if 0 <= grade <= 100:
        letter = grade_students(grade)
        print(f"{name}, you've got a(n) {letter}")
    else:
        print("❌ grade must be between 0 and 100.")

    again = input("Do you want to try again: (yes/no)").lower()
    if again != "yes":
        print("we wish you the best <3, goodbye")
        break
  


def fitness_tracker(steps):
    if steps < 5000:
        return "beginner"
    elif 5000 <= steps < 10000:
        return "intermediate"
    else:
        return "athlete"

while True:
    name = input("Please enter your name: ")
    try:
        steps = int(input("Please enter your daily steps: "))
    except ValueError:
        print("❌ Invalid input, please enter a number.")
        continue

    if 0 <= steps <= 100000:
        fit = fitness_tracker(steps)
        print(f"Hey {name}, you're a/an {fit}!")
    else:
        print("❌ Invalid input, please enter a number between 0 and 100000.")

    again = input("Do you want to try again? (yes/no) ").lower()
    if again != "yes":
        print("Thanks for using our fitness tracker <3!")
        break


def double_number(a):
    return a * 2
number = int(input("enter the number u want to double: "))
result = double_number(number)
print(f"double of this number is {result}")


def greet():
    return f"yo, {name} what's up"
name = input("what's your name? ")
result = greet(name)
print(result)

def greet(name1):
    return f"Hey, {name1} you're unstoppable"
print(greet("omar"))

def triple_number(a):
    return a * 3
num = int(input("enter the number u want to triple: "))
result1 = triple_number(num)
print(f"{num} x {3} = {result1}")


def calculator(a , b ,operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "undfind"
        else:
            return a / b
    else:
        return "invalid operation"
while True:

 a = int(input("enter the first number: "))
 b = int(input("enter the sec number: "))
 operation = input("what operation do you want to do (add,subtract,multiply,divide)? ").lower()
 result2 = calculator(a , b ,operation)
 print(f"result: {result2}")
 
 again1 = input("Do you want to calculate another number? (yes/no)").lower()
 if again1 != "yes":
     print("Thanks for using the calculator <3")
     break
 
 def power_up(base, exponent ):
    return base**exponent
base = int(input("enter the base: "))
exponent = int(input("enter the exponent: "))
result = power_up(base, exponent)
print(f"result :{result}")