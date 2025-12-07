import json
from datetime import date

# Load expenses
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    expenses = []

# Load budget
try:
    with open("budget.json", "r") as file:
        budget = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    budget = None


while True:
    print("\n" + "=" * 40)
    print("        EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View by category")
    print("4. View total spent")
    print("5. Set budget")
    print("6. Check budget status")
    print("7. Exit")
    print("=" * 40)
    
    choice = input("\nChoose an option (1-7): ")
    
    if choice == "1":
        print("\n--- ADD EXPENSE ---")
        category = input("Category (e.g., food, rent, transport): ").strip()
        amount = float(input("Amount (EGP): "))
        description = input("Description: ").strip()
        date_input = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
        expense_date = date_input if date_input else str(date.today())

        expenses.append({
            "category": category,
            "amount": amount,
            "description": description,
            "date": expense_date
        })
        
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print(f"✓ Expense added successfully! ({amount} EGP for {category})")
    
    elif choice == "2":
        if not expenses:
            print("\nNo expenses recorded yet.")
        else:
            print("\n" + "=" * 40)
            print("        ALL EXPENSES")
            print("=" * 40)
            for i, expense in enumerate(expenses, 1):
                print(f"\n#{i}")
                print(f"  Category: {expense['category']}")
                print(f"  Amount: {expense['amount']} EGP")
                print(f"  Description: {expense['description']}")
                print(f"  Date: {expense['date']}")
            print("=" * 40)
    
    elif choice == "3":
        print("\n--- SEARCH BY CATEGORY ---")
        search_category = input("Enter category to search: ").lower().strip()

        found = False
        print("\n" + "=" * 40)
        for expense in expenses:
            if search_category in expense["category"].lower():
                print(f"\nCategory: {expense['category']}")
                print(f"Amount: {expense['amount']} EGP")
                print(f"Description: {expense['description']}")
                print(f"Date: {expense['date']}")
                print("-" * 40)
                found = True

        if not found:
            print(f"No expenses found in category '{search_category}'")
        print("=" * 40)
    
    elif choice == "4":
        if not expenses:
            print("\nNo expenses recorded yet.")
        else:
            total = sum(expense["amount"] for expense in expenses)
            print(f"\n💰 Total spent: {total} EGP")
    
    elif choice == "5":
        print("\n--- SET BUDGET ---")
        budget = float(input("Enter your monthly budget (EGP): "))
        
        with open("budget.json", "w") as file:
            json.dump(budget, file, indent=2)
        
        print(f"✓ Budget set to {budget} EGP")
    
    elif choice == "6":
        print("\n" + "=" * 40)
        print("        BUDGET STATUS")
        print("=" * 40)
        
        if budget is None:
            print("❌ No budget set yet.")
            print("   Use option 5 to set a budget.")
        elif not expenses:
            print(f"Budget: {budget} EGP")
            print("No expenses recorded yet.")
            print(f"Remaining: {budget} EGP (100%)")
        else:
            total = sum(expense["amount"] for expense in expenses)
            remaining = budget - total
            percentage = (remaining / budget) * 100
            
            print(f"Budget: {budget} EGP")
            print(f"Spent: {total} EGP")
            print(f"Remaining: {remaining} EGP ({percentage:.1f}%)")
            print("=" * 40)
            
            if remaining < 0:
                print("⚠️  WARNING: You're OVER BUDGET!")
            elif percentage < 10:
                print("⚠️  WARNING: Less than 10% of budget remaining!")
            elif percentage < 25:
                print("⚠️  CAUTION: Less than 25% of budget remaining.")
            else:
                print("✓ You're within budget.")
        
        print("=" * 40)
    
    elif choice == "7":
        print("\n👋 Goodbye! Your data has been saved.")
        break
    
    else:
        print("\n❌ Invalid choice! Please enter a number between 1-7.")