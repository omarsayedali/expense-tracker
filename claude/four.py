try:

    with open("profile.txt", "r") as file:
        content = file.read()

        print(f"Your saved profile:\n {content}\n")

except FileNotFoundError:
        print("File not found, Creating one....")
        name = input("What's your name? ")
        fav_color = input("What's your favorite colour? ")


        with open("profile.txt", "w") as file:
            file.write(f"Name : {name}\n  Favorite colour : {fav_color}\n")

        print("Profile saved! ")