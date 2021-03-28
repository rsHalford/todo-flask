from app import app
from flask import render_template, make_response

@app.route('/')
def about():
    response = make_response(render_template('about.html'))
    response.mimetype = 'text/plain'
    return response
