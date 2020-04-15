from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy 

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/btech'

  
db = SQLAlchemy(app)   #db object
class sem1(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.String(80), nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.String(120), nullable=False)
class sem2(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.String(80), nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.String(120), nullable=False)
class sem3(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.String(80), nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.String(120), nullable=False)
class sem4(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.String(80), nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.String(120), nullable=False)
class sem5(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.String(80), nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.String(120), nullable=False)
    
    
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/upload")
def upload_papers():
    return render_template("upload_download.html")
@app.route("/about")
def About():
    return render_template("about.html")

@app.route("/getpapers")
def gwtpaper():
    return  render_template("upload_download.html")

#below fxn gets value from drop of semster in upload paper
@app.route("/fetch_sem_upload_download" , methods=['GET', 'POST'])
def return_sem():
    select = request.form['sem']
    select = request.form.get('sem')
    global sem_keep #makin this var global so i can use sem value in other fxns
    sem_keep=str(select) 
    radio_val = request.form['upload_download']
    radio_val=request.form.get('upload_download')
    
    if str(radio_val)=='upload':
        return render_template('uploadtemplate.html',param=str(select),param1=str(radio_val))
    elif str(radio_val=='download'):
        return render_template('paper_show.html',param=str(select),param1=str(radio_val))

@app.route("/upload_papertodb" , methods=['GET', 'POST'])
def upload_papertodb():
    batch_get = request.form['batch']
    batch_get = request.form.get('batch')
    papertype_get = request.form['papertype']
    papertype_get = request.form.get('papertype')
    paper_file = request.form['paper']
    paper_file = request.form.get('paper')
    if(request.method=='POST'):
        entry = sem1(batch=batch_get,paper=paper_file )   #vars are matching to database sem1 cols
        db.session.add(entry)
        db.session.commit()
    

if __name__ == "__main__":
    app.run(debug=True,port=1115)    
