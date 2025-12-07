def even_odd_reader(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
numbers = []
even_count = 0
odd_count = 0

while True:
    user_input = int(input("Enter the number you want to check: (type 'stop' if you want to exit)" ))
    if user_input == "stop".lower():
        print("Goodbye<3...")
        break

    try:
        num = int(user_input)
    except ValueError:
        print("please enter a valid number ")
        continue
    result = even_odd_reader(num)
    print(f"{num} is {result}.")
    if result == "even":
        even_count += 1
    else:
        odd_count += 1
    print(f"\nYou entered {even_count} even and {odd_count} odd numbers.")
    numbers.append(num)
    print(numbers)

    
songs = ["born to die" , "star shopping" , "lose yourself"]
for i , song in range(songs):
    print(f"{i}. {song}")

    








