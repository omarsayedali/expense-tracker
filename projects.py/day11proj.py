from datetime import datetime
from collections import Counter

def write_entry():
    name = input("What's your name? ").strip().title()
    filename = f"{name}.txt"

    mood = input("How are you feeling today? (happy/sad/tired/excited/etc.): ").lower()
    entry = input("Write your journal entry: ").strip()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a") as file:
        file.write(f"[{time}] ({mood}) {entry}\n")

    print(f"✅ Entry saved in {filename}!\n")


def view_personal_journal():
    name = input("Whose journal do you want to read? ").strip().title()
    filename = f"{name}.txt"

    try:
        with open(filename, "r") as file:
            content = file.read()
            if content.strip() == "":
                print("🕳️ This journal is empty.")
            else:
                print(f"\n📖 {name}'s Journal Entries:\n")
                print(content)
    except FileNotFoundError:
        print(f"⚠️ No journal found for {name}.\n")


def search_personal_entries():
    name = input("Whose journal do you want to search? ").strip().title()
    keyword = input("Enter a word, mood, or date to search for: ").lower()
    filename = f"{name}.txt"

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


def view_mood_stats():
    name = input("Whose mood stats do you want to see? ").strip().title()
    filename = f"{name}.txt"

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if not lines:
                print("📉 No entries yet.")
                return

            moods = [line.split("(")[1].split(")")[0].strip() for line in lines if "(" in line and ")" in line]
            mood_counts = Counter(moods)
            total_entries = len(lines)
            last_entry_time = lines[-1].split("]")[0].replace("[", "")

            print(f"\n📊 Mood Statistics for {name}:")
            print(f"🧾 Total entries: {total_entries}")
            print(f"🕒 Last entry: {last_entry_time}")
            print("💬 Mood breakdown:")
            for mood, count in mood_counts.items():
                print(f"   - {mood}: {count} times")
    except FileNotFoundError:
        print(f"⚠️ No journal found for {name}.\n")


def delete_personal_journal():
    name = input("Whose journal do you want to delete? ").strip().title()
    filename = f"{name}.txt"

    confirm = input(f"Are you sure you want to delete {name}'s journal? (yes/no): ").lower()
    if confirm == "yes":
        try:
            open(filename, "w").close()
            print(f"🗑️ {name}'s journal cleared successfully.\n")
        except FileNotFoundError:
            print("⚠️ Journal file not found.")
    else:
        print("❎ Cancelled.\n")


while True:
    print("\n=== PERSONAL MOOD JOURNAL SYSTEM ===")
    print("1. Write a new entry")
    print("2. View someone's journal")
    print("3. Search within a journal")
    print("4. View mood statistics")
    print("5. Delete a journal")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        write_entry()
    elif choice == "2":
        view_personal_journal()
    elif choice == "3":
        search_personal_entries()
    elif choice == "4":
        view_mood_stats()
    elif choice == "5":
        delete_personal_journal()
    elif choice == "6":
        print("👋 Goodbye! Take care of yourself.")
        break
    else:
        print("❌ Invalid choice. Please select 1-6.")
