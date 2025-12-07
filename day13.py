while True:
 
 name = input("What's your name? ")
 weight = int(input("How much do you weigh? "))
 best_lift = input("what's your best lift? ")
 coach = input("what's your coach's name? ")
 team = input("what team are you in? ")
 count = int(input(f"""1. count how many athlete has been added in total
                   2. exit 
                   3. search for an athlete by name
                    (1/2/3):"""))
 if count == 2 :
    print("GOODBYE<3")
    break
 
 athlete = {"name":f"{name}",
 "weight":f"{weight}",
 "coach name":f"{coach}"}
 athlete["best lift"] = f"{best_lift}"
 athlete["team"] = f"{team}"
 for key , value in athlete.items():
     print(f"{key}: {value}")

 with open("athletes.txt", "a") as file:
    file.write(f"name: {name}\n")
    file.write(f"weight: {weight}\n")
    file.write(f"coach name: {coach}\n")
    file.write(f"best lift: {best_lift}\n")
    file.write(f"team :{team}\n")

 with open("athletes.txt", "r") as file:
     content = file.read()
     print("\n📄 File content so far:\n")
     print(content)

 if count == 1 :
     with open("athletes.txt", "r") as file:
             total_athletes = sum(1 for line in file if line.startswith("name: "))
             print(f"📊 Total entries in your app so far is: {total_athletes}")

 elif count == 3 :
     name1 = input("Which athlete do you want to search? ").strip().title()
     keyword = input("Enter a word, best lift, or coach name to search for: ").lower()
     filename = "athletes.txt"

     found = False
     try:
        with open("athletes.txt", "r") as file:
            for line in file:
                if keyword in line.lower():
                    print(line.strip())
                    found = True
        if not found:
            print("🔍 No matching athlete found.")
     except FileNotFoundError:
        print(f"⚠️ No athlete named {name1}.\n")
 