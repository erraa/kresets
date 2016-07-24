from app import app

@app.route('/')
@app.route('/index')

def index():
    return "Testing 1235456"
