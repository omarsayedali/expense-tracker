user = {}

user["name"] = input("Please enter your name: ")
user["age"] = int(input("Please enter your age: "))
user["city"] = input("what city are you from: ")

print(user)
print(f"Hello {user["name"]}, you are {user["age"]} years old and live in {user["city"]}")

#----------------------------------------------------------------------------------------------

inventory = {"apples": 100, "oranges": 80, "kiwis": 75}

print("Current inventory:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")

product = input("\nWhat do you want to buy? ").lower()
amount = int(input("How many do you want to buy? "))

if product in inventory:
    if inventory[product] >= amount:
        inventory[product] -= amount
        print("\nUpdated inventory:")
        for product, quantity in inventory.items():
            print(f"{product}: {quantity}")
    else:
        print(f"\nNot enough stock! We only have {inventory[product]} {product}.")
else:
    print("\nProduct not found.")

#---------------------------------------------------------------------------------------------------


students = {
    "student1": {"name": "Ahmed", "grades": [85, 90, 78]},
    "student2": {"name": "Omar", "grades": [92, 88, 95]},
    "student3": {"name": "Sara", "grades": [70, 75, 80]}
}

for student_id, info in students.items():
    name = info["name"]
    grades = info["grades"]
    average = sum(grades) / len(grades)
    print(f"{name}'s average: {average:.2f}")

lowest_name = ""
lowest_avg = 100


for student_id, info in students.items():
    avg = sum(info["grades"]) / len(info["grades"])
    if avg < lowest_avg:
        lowest_avg = avg
        lowest_name = info["name"]

print(f"\nlowest average: {lowest_name} with {lowest_avg:.2f}")





students1 = {
    "s1": {"name": "Ahmed", "gpa": 3.5},
    "s2": {"name": "Sara", "gpa": 3.9},
    "s3": {"name": "Omar", "gpa": 3.2}
}

highest_name = ""
highest_gpa = 0

for headline, content in students1.items:
    if content["gpa"] > highest_gpa:
        highest_gpa = content["gpa"]
        highest_name = content["name"]

print(f"\nhighest gpa: {highest_name} with {highest_gpa:.2f}")