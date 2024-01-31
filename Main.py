from flask import  *
#import sqlite3
#import hashlib
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('singup')
def index():
    return render_template('singup.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
