fruits = ["apple", "banana", "kiwi", "passion fruit", "mango"]
fruits.append("orange")
fruits.pop(2)
fruits.sort()
print(fruits[:3])

students = {"omar": 95, "zaina":65, "bakr":88}
students["marwan"]= 78
students["bakr"]= 66
for name, score in students.items():
    print(f"{name}: {score}")


def invitation(name, invitaion= "you're invited"):
    print(f"{invitaion}, {name}!")
invitation("omar")


def total(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
total(8,9,2, name="omar", age=18)


def calculations(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, count, average
t , c , av=calculations([20, 4, 5])
print(t, c ,av)



users = {}

while True:
    name = input("Please enter your name: ")

    try:
        steps = int(input("Please enter your daily steps: "))
        if steps < 0:
            print("❌ Steps cannot be negative.")
            continue
    except ValueError:
        print("❌ Invalid input, please enter a number.")
        continue

    users[name] = steps

 
    again = input("Do you want to enter another user? (yes/no) ").lower()
    if again != "yes":
        print("Thanks for using our fitness tracker <3.")
        break


view = input("Do you want to view all users and their steps? (yes/no) ").lower()
if view == "yes":
    print("All users and steps:")
    for user, step in users.items():
        print(f"{user}: {step} steps")
