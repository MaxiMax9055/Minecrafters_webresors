from flask import  *
#import sqlite3
#import hashlib
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('downloadm.html')
@app.route('/license')
def license ():
    return render_template('licens.html')
@app.route('/win10,11')
def win1011 ():
    return render_template('mineinstall.exe')
@app.route('/winold')
def winold ():
    return render_template('oldinstall.msi')
@app.route('/macos')
def macos ():
    return render_template('mineinstall.dmg')
@app.route('/lindeb')
def lindeb ():
    return render_template('Minecraft.deb')
@app.route('/linall')
def linall ():
    return render_template('Minecraft.tar.gz')
@app.route('/launcher')
def launcher ():
    return render_template('launcher.exe')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
