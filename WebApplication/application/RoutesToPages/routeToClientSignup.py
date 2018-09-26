from flask import render_template
from flask import request,redirect
from application import app
from application import userController, adminController
from application import databaseObject as db

import random 

@app.route('/clientSignup')
def clientSignup():
	return render_template('clientSignup.html')


@app.route('/signupForm', methods=['POST'])
def processSignup():

	firstname = request.form["firstname"]
	lastname = request.form["lastname"]
	phonenumber = request.form["phonenumber"]
	email = request.form["email"]
	username = request.form["username"]
	password = request.form["password"]
	address = request.form["address"]


	userController.createClient(firstname,lastname,address,phonenumber,email,username,password,0,0,0)
	return redirect("/")
