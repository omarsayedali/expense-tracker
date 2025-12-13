from flask import Flask , render_template, request, redirect
import json
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    
    try:
        with open("budget.json", "r") as file:
            budget_data = json.load(file)
            
            
            if isinstance(budget_data, dict):
    

               if 'monthly_budget' in budget_data:
                   current_budget = budget_data['monthly_budget']
               else:
                   current_budget = 'Not set'
            else:
                current_budget = 'Not set'
                
    except (FileNotFoundError, json.JSONDecodeError):
        current_budget = 'Not set'
    print(f"DEBUG: current_budget = {current_budget}")
    return render_template('home.html', current_budget=current_budget)

@app.route('/about')
def about():
    return "This is my about page, Hey i'm learning Flask"

@app.route('/contact')
def contact():
    return "You can contact me on, Email: omarayed5745@gmail.com"


@app.route('/expenses')
def expenses():
    filter_category = request.args.get('category', 'All')
    
    try:
        with open("expenses.json", "r") as file: 
            expense_list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError): 
        expense_list = []
    
    if filter_category != 'All':
        expense_list = [expense for expense in expense_list if expense['category'] == filter_category]
    
    # CALCULATE TOTAL FIRST ← Line 38
    total = sum(expense['amount'] for expense in expense_list)
    
    # NOW LOAD BUDGET AND DO CALCULATIONS ← Must come AFTER total
   # LOAD BUDGET
    try:
        with open("budget.json", "r") as file:
         budget_data = json.load(file)
        # Make sure budget_data is a dict, not a number
         if isinstance(budget_data, dict):
             MONTHLY_BUDGET = budget_data.get('monthly_budget', 10000)
         else:
             MONTHLY_BUDGET = 10000
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        MONTHLY_BUDGET = 10000 
    
    # BUDGET LOGIC (now total is defined)
    if MONTHLY_BUDGET > 0:
        budget_percentage = (total / MONTHLY_BUDGET) * 100
    else:
        budget_percentage = 0
    
    if budget_percentage >= 90:
        budget_status = "danger"
        budget_message = "⚠️Warning: You've spent $" + str(round(total, 1)) + " / $" + str(MONTHLY_BUDGET) + " (" + str(round(budget_percentage, 0)) + "% of budget)"
    elif budget_percentage >= 70:
        budget_status = "warning"
        budget_message = "⚡Caution: You've spent $" + str(round(total, 1)) + " / $" + str(MONTHLY_BUDGET) + " (" + str(round(budget_percentage, 0)) + "% of budget)"
    else:
        budget_status = "safe"
        budget_message = "✅Safe: You've spent $" + str(round(total, 1)) + " / $" + str(MONTHLY_BUDGET) + " (" + str(round(budget_percentage, 0)) + "% of budget)"
    
    # LOAD CATEGORIES FOR DROPDOWN
    try:
        with open("expenses.json", "r") as file: 
            all_expenses = json.load(file)
        categories = sorted(set(expense['category'] for expense in all_expenses))
    except:
        categories = []
    
    return render_template('expenses.html', 
                         expenses=expense_list, 
                         total=total, 
                         categories=categories, 
                         current_filter=filter_category,
                         budget_message=budget_message,
                         budget_status=budget_status)

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', user_name=name)

@app.route('/square/<int:number>')
def square(number):
    square_number = number**2
    return f"The square of {number} is {square_number}"

@app.route('/add-expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST' :
        category = request.form['category']
        amount = float(request.form['amount'])
        description = request.form['description']
        expense_date = str(date.today())

        try:
            with open("expenses.json", "r") as file:
                expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            expenses = []

        if expenses:
            new_id = max(expense['id'] for expense in expenses) + 1
        else:
            new_id = 1

        expense = {
            "id" : new_id,
            "category": category,
            "amount": amount,
            "description": description,
            "date": expense_date
        }

        expenses.append(expense) 

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        
        return redirect ('/expenses')
    
    return render_template('add_expense.html')


@app.route('/set-budget', methods=['POST'])
def set_budget():
    budget_amount = float(request.form['budget'])

    with open ("budget.json", "w") as file:
        json.dump({"monthly_budget" : budget_amount}, file)

    return redirect('/')


@app.route('/delete/<int:expense_id>')
def delete_expense(expense_id):
    try:
        with open("expenses.json" ,"r") as file:
            expenses = json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        expenses = []
          
    expenses = [expense for expense in expenses if expense['id'] != expense_id]

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    return redirect('/expenses')

@app.route('/edit/<int:expense_id>')
def edit_expense(expense_id):
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []

    expense_to_edit = None
    for expense in expenses:
        if expense['id'] == expense_id:
            expense_to_edit = expense
            break

    if not expense_to_edit:
        return redirect('/expenses')
    
    return render_template('edit_expense.html', expense=expense_to_edit)

@app.route('/update/<int:expense_id>', methods=['POST'])
def update_expense(expense_id):
    
    category = request.form['category']
    amount = float(request.form['amount'])
    description = request.form['description']

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except (FileNotFoundError , json.JSONDecodeError):
        expenses = []

    for expense in expenses:
        if expense['id'] == expense_id:
            expense['category'] = category
            expense['amount'] = amount
            expense['description'] = description
            break

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    return redirect('/expenses')


if __name__ == '__main__' :
    import os
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)

@app.route('/health')
def health():
    return 'OK', 200