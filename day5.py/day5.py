while True:
    number = int(input("enter a number:"))
    end = int(input("how many multiplications u want:"))
    count = 1
    while count <= end:
        print(f"{number} x {count} = {number * count}")
        count = count + 1

    again = input("do you want to enter another number (yes/no) ?")
    if again.lower() != "yes":
     print("thanks for trying our multiplication calculator")
     break
   
while True:
    number = int(input("enter a number:"))
    end = int(input("how many multiplications u want:"))
    count = 1
    step = int(input("enter the step (1 for normal, 2 for skipping, etc...)"))
    for count in range(1 , end+1, step):
       print(f"{number} x {count} = {number * count}")

    again = input("do you want to enter another number (yes/no) ?")
    if again.lower() != "yes":
     print("thanks for trying our multiplication calculator")
     break

while True:
    number = int(input("enter a number:"))
    end = int(input("how many multiplications u want:"))
    count = 1
    step = int(input("enter the step (1 for normal, 2 for skipping, etc...)"))
    order = input("Do you want ascending or descending order (a/d)? ")
    
    if order.lower() == "a":
       for count in range(1 , end+1, step):
           print(f"{number} x {count} = {number * count}")

    else:
         for count in range(end , 0, -step):
             print(f"{number} x {count} = {number * count}")

    again = input("do you want to enter another number (yes/no) ?")
    if again.lower() != "yes":
     print("thanks for trying our multiplication calculator")
     break

