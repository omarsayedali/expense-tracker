from flask import Flask , render_template, request, redirect
from datetime import date
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///expenses.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Expense {self.description}>'


# The Budget Model (Just one row to store the limit)
class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    # 1. Fetch the budget from the Database
    budget_record = Budget.query.first()
    
    if budget_record:
        current_budget = budget_record.amount
    else:
        current_budget = 0 # Or "Not Set"

    # 2. Pass it to the HTML
    return render_template('home.html', current_budget=current_budget)



@app.route('/expenses')
def expenses():
    # 1. Get the filter from the URL (default to 'All')
    filter_category = request.args.get('category', 'All')

    # 2. Query the Database (No more JSON loops!)
    if filter_category == 'All':
        expenses_list = Expense.query.all()
    else:
        expenses_list = Expense.query.filter_by(category=filter_category).all()

    # 3. Calculate Total
    total = sum(expense.amount for expense in expenses_list)

    # 4. Get Unique Categories for the Dropdown
    # We query all expenses just to get the list of categories
    all_expenses = Expense.query.all()
    categories = sorted(list(set(e.category for e in all_expenses)))

        # --- NEW BUDGET LOGIC (Database) ---
    budget_record = Budget.query.first()
    if budget_record:
        MONTHLY_BUDGET = budget_record.amount
    else:
        MONTHLY_BUDGET = 1000.0 # Default

    # 5. Calculate Budget Status
    if MONTHLY_BUDGET > 0:
        budget_percentage = (total / MONTHLY_BUDGET) * 100
    else:
        budget_percentage = 0

    if budget_percentage >= 90:
        budget_status = "danger"
        budget_message = f"Warning: You've spent ${round(total, 1)} / ${MONTHLY_BUDGET}"
    elif budget_percentage >= 70:
        budget_status = "warning"
        budget_message = f"Caution: You've spent ${round(total, 1)} / ${MONTHLY_BUDGET}"
    else:
        budget_status = "safe"
        budget_message = f"Safe: You've spent ${round(total, 1)} / ${MONTHLY_BUDGET}"

    # 6. Render
    return render_template('expenses.html', 
                           expenses=expenses_list, 
                           total=total,
                           categories=categories,
                           current_filter=filter_category,
                           budget_message=budget_message,
                           budget_status=budget_status)

@app.route('/add-expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        # 1. Get Form Data
        category = request.form['category']
        amount = float(request.form['amount'])
        # NOTE: Your old code used 'description', make sure you match it here
        title = request.form['description'] 
        
        # Date: Use today's date automatically or get from form
        # If your HTML doesn't have a date field, use this:
        from datetime import date
        expense_date = str(date.today())

        # 2. Save to Database (The Magic)
        new_expense = Expense(description=title, amount=amount, category=category, date=expense_date)
        db.session.add(new_expense)
        db.session.commit()

        # 3. Go back to list
        return redirect('/expenses') # Or whatever your home route is called

    return render_template('add_expense.html')


@app.route('/set-budget', methods=['POST'])
def set_budget():
    new_amount = float(request.form['budget'])
    
    # Check if a budget already exists
    budget = Budget.query.first()
    
    if budget:
        # Update existing
        budget.amount = new_amount
    else:
        # Create new
        budget = Budget(amount=new_amount)
        db.session.add(budget)
        
    db.session.commit()
    return redirect('/expenses')


@app.route('/delete/<int:id>')
def delete_expense(id):
    
    expense_to_delete = Expense.query.get_or_404(id)

    db.session.delete(expense_to_delete)
    db.session.commit()

    
    return redirect('/expenses')

# 1. Show the Edit Form
@app.route('/edit/<int:id>')
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    return render_template('edit_expense.html', expense=expense)

# 2. Process the Update
@app.route('/update/<int:id>', methods=['POST'])
def update_expense(id):
    expense = Expense.query.get_or_404(id)
    
    expense.category = request.form['category']
    expense.amount = float(request.form['amount'])
    expense.description = request.form['description'] # Assuming you renamed title -> description in Model
    
    db.session.commit()
    return redirect('/expenses')

@app.route('/health')
def health():
    return 'OK', 200

with app.app_context():
    db.create_all()


if __name__ == '__main__' :
    import os
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)

