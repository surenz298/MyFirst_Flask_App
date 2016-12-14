#!/usr/bin/python
from flask import render_template, request, redirect, url_for
import Prime , json
from app import app
from app import db, models
from sqlalchemy import text

history = {}

@app.route('/history')
def hist():
	histo = models.Hist.query.all()
	return render_template('history.html',history=histo)


@app.route('/check/<number>')
def check(number):
	value = Prime.isprime(number)
	v = models.Hist(number=number,comment=value)
	db.session.add(v)
	db.session.commit()
	return render_template('prime_checker.html',prime=value,number=number)

@app.route('/',methods=['GET','POST'])
def home():
	error = None
	if request.method == "POST":
		x = request.form["number"]
		return redirect (url_for('check',number=x))

	return render_template('prime_checker.html',error=error)
