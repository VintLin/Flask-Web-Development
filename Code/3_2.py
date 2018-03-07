# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 20:45:26 2018

@author: 11796
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
