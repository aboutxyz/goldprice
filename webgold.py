#coding:utf-8

from flask import Flask
import mako

app = Flask(__name__)
mako = MakoTemplates(app)

@app.route('/')
def hello():
    return render_template('index.html', name = 'mako')
    
if __name__ == '__main__':
    app.run()