#!/usr/bin/env python
#-*- coding: utf-8 -*-


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Helo Flask'

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return 'Profile page of user #{}'.format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    return 'All books in {} category'.format(genre)

if  __name__=="__main__":
    app.run(debug=True)     #включен режим отладки 
 
