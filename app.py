# Web Development with Flask:

# A simple webpage using Flask to collect user data with MongoDBatlas for data storage:

from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

application = Flask(__name__)

# MongoDB setup using MongodbAtlas
client = MongoClient('mongodb+srv://detlaalade:cAJkpMdK1jIp37RP@finalproject.b403o.mongodb.net/?retryWrites=true&w=majority&appName=FinalProject')
db = client['income_analysis']
collection = db['survey_data']

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission
        try:
            age = int(request.form['age'])
            gender = request.form['gender']
            total_income = float(request.form['total_income'])

            # Expense Categories
            expenses = {}
            expense_categories = {
                'utilities': 'utilities_cb',
                'entertainment': 'entertainment_cb',
                'school_fees': 'school_fees_cb',
                'shopping': 'shopping_cb',
                'healthcare': 'healthcare_cb'
            }
            
            for category, checkbox in expense_categories.items():
                if request.form.get(checkbox):  # Only if the checkbox is checked
                    amount_str = request.form.get(category)
                    if amount_str:  # Only convert to float if not empty
                        expenses[category] = float(amount_str)
                    else:
                        expenses[category] = 0.0

            # Insert into MongoDBatlas
            survey_data = {
                'age': age,
                'gender': gender,
                'total_income': total_income,
                'expenses': expenses
            }
            collection.insert_one(survey_data)
            return redirect(url_for('thank_you'))
        except ValueError:
            return "Please enter valid data."

    return render_template('index.html')

@application.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    application.run(debug=True, use_reloader=False)
