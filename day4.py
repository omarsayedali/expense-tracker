count = 1
while count <= 5:
    print("Hello!", count)
    count = count + 1
count1 = 1
while count1 <= 10:
    print(count1)
    count1 = count1 + 1
count2 = 2
while count2 <= 20:
    print(count2)
    count2 = count2 + 2
count3 = 1
while count3 <= 20:
    print(count3)
    count3 = count3 + 2
count4 = 1
while count4 <= 10:
    print(count4 * 5)
    count4 = count4 + 1
number = 1
while number <= 5:
    print(number)
    number = number + 1
number1 = 2
while number1 <= 10:
    print(number1)
    number1 = number1 + 2
number2 = 1
while number2 <= 5:
    print(number2 * 3)
    number2 = number2 + 1
num = 10
while num >= 0:
    print(num)
    num = num - 1
num2 = 1
while num2 <= 10:
    print(num2 * 2)
    num2 = num2 + 2
num3 = 1
while num3 <= 12:
    print(f"7 x {num3} = {num3 * 7}")
    num3 = num3 + 1
while True: 
 num4 = int(input("enter a number: "))
 end = int(input("enter the range (how far you want the table to to go): "))
 count5 = 1
 while count5 <= end:
    print(f"{num4} x {count5} = {num4 * count5}")
    count5 = count5 + 1 
    
 again = input("Do you want another table? (yes/no): ")
 if again.lower() != "yes":
     print("thanks for using the multiplication table generator! 👋")
     break