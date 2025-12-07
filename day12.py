entries = []
from datetime import datetime

while True:
    print(50 * "-", "Welcome to our journal", 50 * "-")
    try:
        choice = int(input(f"""Please choose what you want to do:
                   1. Enter a new entry
                   2. Show all entries you've entered so far
                   3. Show how many entries you've made in total
                   4. Exit program 
                   5. Search for specific entry
                   6. Delete all entries
                   (1, 2, 3, 4, 5, 6): """))
    except ValueError:
         print("❌ Please enter a number between 1 and 6.")
         continue  

    if choice == 4:

        print(50 * "*", "Thanks for using our journal. Goodbye...", 50 * "*")
        break

    elif choice == 1:
        name = input("Please enter your name: ")
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
        entry = input("Please enter what you want to save in your journal (type 'break' to exit): ")

        if entry.lower() == "break":
            print(50 * "*", "Thanks for using our journal. Goodbye...", 50 * "*")
            break

        entries.append(entry)

        with open("entries.txt", "a") as file:
            file.write(f"name: {name}\n")
            file.write(f"time: {time}\n")
            file.write(f"entry: {entry}\n")
            file.write("-" * 40 + "\n")
        print("✅ Entry added successfully!")

    elif choice == 2:
        print("📖 Entries you added this session:")
        for i, entry in enumerate(entries, start=1):
            print(f"{i}. {entry}")

        with open("entries.txt", "r") as file:
            print("\n📚 Entries saved in file:")
            print(file.read())

    elif choice == 3:
        with open("entries.txt", "r") as file:
            total_entries = sum(1 for line in file if line.startswith("entry:"))
            print(f"📊 Total entries in your journal so far: {total_entries}")

    elif choice == 5:
        name = input("Whose journal do you want to search? ").strip().title()
        keyword = input("Enter a word or a date to search for: ").lower()
        filename = "entries.txt"

        found = False
        try:
            with open(filename, "r") as file:
                for line in file:
                    if keyword in line.lower():
                        print(line.strip())
                        found = True
            if not found:
                print("🔍 No matching entries found.")
        except FileNotFoundError:
            print(f"⚠️ No journal found for {name}.\n")


    elif choice == 6:
        confirm = input("Are you sure you want to delete all entries? (yes/no): ").lower()
        if confirm == "yes":
           with open("entries.txt", "w") as file:
              pass  
           print("🗑️ All entries deleted successfully!")
        else:
         print("❌ Deletion cancelled.")

    
    else:
        print("Wrong input, Goodbye...")
        break


