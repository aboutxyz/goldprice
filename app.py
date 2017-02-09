#coding:utf-8

from flask import Flask
from flask_mako import MakoTemplates, render_template

app = Flask(__name__)
mako = MakoTemplates(app)

@app.route('/')
def index():
    return render_template('index.html', name = 'mako')
    
if __name__ == '__main__':
    app.run(port = 8989)