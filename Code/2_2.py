# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 22:03:02 2018

@author: 11796
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world!</h1>'
