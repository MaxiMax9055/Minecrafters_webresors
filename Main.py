from flask import  *
#import sqlite3
#import hashlib
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/license')
def license ():
    return render_template('licens.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
