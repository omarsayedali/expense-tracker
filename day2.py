age = int(input("enter your age: "))
if age >= 18:
    print("you can vote")
else:
    print("you are too young to vote")
try:
    number = int(input("enter a number: "))
    if number % 2 == 0:
        print("number is even")
    else:
        print("number is odd")
except ValueError:
    print("this is not a valid integer. try again")
age = int(input("enter your age: "))
if age < 13:
    print("you are a child")
elif age < 18:
     print("you are a teenager")
else:
    print("you are an adult")
number1 = int(input("enter number 1: "))
number2 = int(input("enter number 2: "))
if number1 > number2:
    print("the bigger number is", number1)
elif number2 > number1:
    print("the bigger number is", number2)
else:
    print("both numbers are equal")
score = int(input("enter your score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")