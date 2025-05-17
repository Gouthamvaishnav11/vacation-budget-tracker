from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    amount = db.Column(db.Float)

@app.route('/')
def index():
    expenses = Expense.query.all()
    total = sum(exp.amount for exp in expenses)
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['POST'])
def add_expense():
    name = request.form['name']
    amount = float(request.form['amount'])
    new_expense = Expense(name=name, amount=amount)
    db.session.add(new_expense)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    return render_template('update.html', expense=expense)

@app.route('/update/<int:id>', methods=['POST'])
def update_expense(id):
    expense = Expense.query.get_or_404(id)
    expense.name = request.form['name']
    expense.amount = float(request.form['amount'])
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
