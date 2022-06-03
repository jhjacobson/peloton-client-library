from peloton import app
from flask import render_template, redirect, url_for, flash
from .peloton import workouts_db

from flask import render_template, redirect, url_for, flash

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/workouts')
def workouts_page():
    all_workouts = workouts_db.find()
    print('test')
    print(all_workouts)
    return render_template('workouts.html', workouts=all_workouts)