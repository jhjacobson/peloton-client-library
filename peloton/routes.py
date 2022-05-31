from peloton import app
from flask import render_template, redirect, url_for, flash

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/workouts')
def workouts_page():
    return render_template('workouts.html')