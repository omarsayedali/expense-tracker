import json

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = []
except json.JSONDecodeError:
    contacts = []  

while True:
    print("\n1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone number: ")
        email = input("Enter Email: ")

        contacts.append({"name": name
                         , "phone": phone,
                           "email": email})
        
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)

        print("Contact added!")
    
    elif choice == "2":
        for contact in contacts:
            print(contact)
        
    elif choice == "3":
        search_name = input("Enter name to search: ").lower()

        found = False

        for contact in contacts:
             if search_name in contact["name"].lower(): 
                 print(f"\nFound:")
                 print(f"Name: {contact['name']}")
                 print(f"Phone: {contact['phone']}")
                 print(f"Email: {contact['email']}")
                 found = True

        if not found:
             print("No contacts found")
        
    elif choice == "4":

        print("Goodbye!")
        break
    else:

        print("Invalid choice")