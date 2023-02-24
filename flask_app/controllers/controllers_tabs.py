from flask_app import app
from flask import render_template, session, redirect, request, flash

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')