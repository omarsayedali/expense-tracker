while True:

     num = int(input("Please enter a number between 1 and 10: "))
     if num < 1 or num > 10:
       continue
     else:
         break


while True:
    num1 = int(input("please enter a number (Exit enter (-1)): "))
    if num1 != -1:
        print(f"You've entered: {num1}")
        continue
    else:
        print("Goodbye...")
        break


for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")


        