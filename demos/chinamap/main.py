#!/usr/bin/env python

from flask import Flask, render_template

app = Flask('Map Demo')
app.debug=True

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'HELLO WORLD'

@app.route('/v1', methods=['GET', 'POST'])
def map_01():
    return render_template('map-bar-morph.html')

@app.route('/v2', methods=['GET', 'POST'])
def map_02():
    return render_template('map2.html')

if __name__ == '__main__':
    app.run(host='localhost',port=5000)