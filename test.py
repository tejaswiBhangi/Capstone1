from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
# engine = create_engine('mysql+pymysql://root:Avatar16@localhost:3306/tractortek_salestracking')

# engine.connect()
# print(engine)

class SalesForm(FlaskForm):
	itemCode = StringField('Enter item code:')
	empId = StringField('Enter your employee id:')
	date = DateField('Enter today\'s date:', format='%Y-%m-%d')
	quantity = IntegerField('Enter the amount of product(s) sold:')
	submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():
	itemCode = False
	empId = False
	date = False
	quantity = False
	form = SalesForm()
	if form.validate_on_submit():
		itemCode = form.itemCode.data
		empId = form.empId.data
		date = form.date.data
		quantity = form.quantity.data
		form.itemCode.data = ''
		form.empId.data = ''
		form.quantity.data = ''

	return render_template('input.html', form = form, itemCode=itemCode, empId = empId, date = date, quantity = quantity)

if __name__ == '__main__':
	app.run(debug = True)
