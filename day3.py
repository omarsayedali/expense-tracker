name = input("what's your name? ")
print("welcome back", name )
number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number:"))
print("sum of numbers is" , number1 + number2)
age = int(input("how old are you? "))
print("you are going to be", age+10 ,"in 10 years")
food = input("what you favorite food? ")
color = input("what's your favorite color? ")
print("your favorite food is", food ,"and your favorite color is", color)
number = int(input("enter a number:"))
print("double of this number is", number*2)
print("triple of this number is", number*3)
length = int(input("enter the length:"))
width = int(input("enter the width:"))
print("area =", length*width )
print("perimeter =", 2*(length+width))
print("square root of length=", length**0.5)
number3 = int(input("enter a number:"))
print("square of this number is", number3**2)
print("square root of this number is", number3**0.5)
print("the cube of this number is", number3**3)
print(f"square of this number is {number3**2} square root of this number is {number3**0.5}, the cube of this number is {number3**3} ")
name2 = input("what's your name? ")
sport = input("what's your fav sport? ")
num4 = input("what's your fav number? ")
print(f"""hello, your name is {name2},
your favorite sport is {sport},
your favorite number is {num4}.""")
name3 = input("what's your name? ")
hobby = input("what's your favorite hobby? ")
movie = input("what's your favorite movie? ")
print(f"""Hello, {name3}!
your favorite hobby is {hobby}
your favorite movie is {movie}""")

print("="*50)
print("Hi! Let's talk about your dreams ✨ ")
print("="*50)
name4 = input("what's your name? ").title()
while name4.strip() == "":
    name4 = input("please enter a valid name: ")
job = input("what's your dream job? ").title()
while job.strip() == "":
    job = input("please enter a valid dream job: ")
city =input("what's your favorite city? ").title()
while city.strip() == "":
    city = input("please enter a valid city: ")
if job.lower() == "doctor":
    print(f"""Hello, {name4}!
one day, you're gonna acheive your dreams and hopefully become a {job} which is gonna allow you to help a lot of people.
And then you're gonna travel all over the world, and you'd buy a house in {city}, and live there happily for the rest of your life.""")
elif job.lower() == "artist":
     print(f"""Hello, {name4}!
one day, you're gonna acheive your dreams and hopefully become an {job} and you're gonna convert all your emotions into beautiful art.
And then you're gonna travel all over the world, and you'd buy a house in {city}, and live there happily for the rest of your life.""")
else: 
    print(f"""Hello, {name4}!
one day, you're gonna acheive your dreams and hopefully become a/an {job} that's a great goal.
And then you're gonna travel all over the world, and you'd buy a house in {city}, and live there happily for the rest of your life.""")
print("*"*50)
print("Thanks, for sharing your dreams!")
print("*"*50)
