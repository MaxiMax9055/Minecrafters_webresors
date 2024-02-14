from flask import  *
#import sqlite3
#import hashlib
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/sha')
def sha():
    return render_template('sha.html')
@app.route('/vit')
def vit():
    return render_template('vit.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
