from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    posts = [{'body': 'ONYXIA'}, {'body', 'ZG'}]
    wberg = {'wberg': 'Wbergs Mamma'}
    return render_template('index.html',
                           title='Home',
                           wberg=wberg,
                           posts=posts
                           )
