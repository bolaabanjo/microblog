from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bola'}
    posts = [
        {
            'author': {'username': 'Alice'},
            'body': 'This is my first post!'
        },
        {
            'author': {'username': 'Bob'},
            'body': 'Hello everyone, this is Bob!'
        }
        {
            'author': {'username': 'Roy'},
            'body': 'Hi there, my name is Roy!'
        }
        {
            'author': {'username': 'Banjo'},
            'body': 'Have you seen the avengers?'
        },
        {
            'author': {'username': 'Marley'},
            'body': 'Do you play my music?'
        }
    ]
    return render_template('index.html', user=user, posts=posts)