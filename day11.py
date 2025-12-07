from datetime import datetime

while True:
    name = input("what's your name? ")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("first file.txt", "a") as file:
        file.write(f"[{now}] today's the first day of {name} learning about files\n")
        file.write("i think it's easy but you just need to get it first.\n")

        name2 = input("enter your name again (or type 'break' to exit): ")
        if name2.lower() == "break":
            print("Goodbye...")
            break

        file.write(f"[{now}] added this line cuz me {name2} learning the append skill\n")

    with open("first file.txt", "r") as file:
        content = file.read()
        print("\n📄 File content so far:\n")
        print(content)



from datetime import datetime

while True:
    name1 = input("what's your name? ")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
    entry = input("please enter what do you want to save in your journal: (if you want to exit enter 'break') ")

    with open("journal.txt", "a") as file:
        file.write(f"""name: {name1}.
                   entery: {entry}.
                   date:{time}""")
        if entry.lower() == "break":
            print("Goodbye...")
            break
        with open("journal.txt", "r")as file:
            content1 = file.read()
            print("\n📄 File content so far:\n")
        print(content1)



            