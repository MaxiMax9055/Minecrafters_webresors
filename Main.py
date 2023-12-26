from flask import  *
#import sqlite3
#import hashlib
app = Flask(__name__)
list_versions = ["1.7.10","1.8.0","1.10.0","1.11.4","1.12.2","1.13.2","1.14.4","1.15.5","1.16.2","1.16.5","1.17.3","1.18.2","1.19.3","1.19.9","1.20.0","1.20.1"]
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/license')
def license ():
    return render_template('licens.html')

@app.route('/download', methods=['GET','POST'])
def download ():
    if request.method == 'POST':
        selsct_versions = request.form.getlist('versions')
        print(selsct_versions)
        return redirect("/download_thankyou")
    else:
        return render_template('download.html', list_versions=list_versions)
@app.route('/download_thankyou')
def download_thankyou ():
    return render_template('download_thankyou.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
