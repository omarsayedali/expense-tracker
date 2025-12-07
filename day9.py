friends = ["bakr", "mego", "nasser", "maro", "dodo"]

while True:
    print("\n📜 Your current friend list:")
    for i, friend in enumerate(friends, start=1):
        print(f"{i}. {friend}")

    print("\nChoose an action:")
    print("1. Add a new friend")
    print("2. Remove a friend")
    print("3. Exit")

    choice = input("👉 Choose an option (1/2/3): ").strip()

    if choice == "1":
        new_friend = input("What's your new friend's name? ").strip().lower()
        friends.append(new_friend)
        print(f"✅ {new_friend.title()} has been added to your friends list!")

    elif choice == "2":
        delete_friend = input("Enter the name of the person you want to remove: ").strip().lower()
        if delete_friend in friends:
            friends.remove(delete_friend)
            print(f"❌ {delete_friend.title()} has been removed successfully.")
        else:
            print("⚠️ That name isn't in your friends list.")

    elif choice == "3":
        print("👋 Goodbye, see you later!")
        break

    else:
        print("⚠️ Invalid choice! Please enter 1, 2, or 3.")


