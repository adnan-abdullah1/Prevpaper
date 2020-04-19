from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy 
import pymysql
#from sqlalchemy.orm import sessionmaker
#from snowflake.sqlalchemy import URL
#from sqlalchemy.dialects import registry
#from sqlalchemy import create_engine
import sqlalchemy.dialects.sqlite

app=Flask(__name__)
#registry.register('snowflake', 'snowflake.sqlalchemy', 'dialect')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///paper11.db"#"mysql+pymyql://root:admin@127.0.0.1/btech"

db = SQLAlchemy(app)   #db object

class sem1(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem2(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
   
class sem3(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.Integer, nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem4(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem5(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem6(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)

class sem7(db.Model):

    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem8(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.LargeBinary, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
    
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/upload")
def upload_papers():
    return render_template("upload_download.html",param_btn="upload",param="Upload your papers make selection appropriately")
@app.route("/about")
def About():
    return render_template("about.html")

@app.route("/getpapers")
def gwtpaper():
    return  render_template("upload_download.html",param_btn="get-papers",param="Download your papers make selection appropriately")



#below fxn gets value from drop of semster in upload paper
@app.route("/fetch_sem_upload_download" , methods=['GET', 'POST'])
def return_sem():
    select = request.form['sem']
    select = request.form.get('sem')
    #makin this var global so i can use sem value in other fxns
    global sem_keep
    sem_keep=str(select) 
    radio_val = request.form['upload_download']
    radio_val=request.form.get('upload_download')
    if str(radio_val)=='upload':
        return render_template('uploadtemplate.html',param=str(select),param1=str(radio_val))
    elif str(radio_val=='download'):
        all_papers=query.filter_by().all()
        return render_template('paper_show.html',param=all_papers)
def database_commit(entry):
    db.create_all()  
    db.session.add(entry)
    db.session.commit()
    
@app.route("/upload_papertodb" , methods=['GET', 'POST'])
def upload_papertodb():
    batch_get = request.form['batch']
    papertype_get = request.form['papertype']
    
    paper_file = request.files['paper'].read()#request.files['paper']
    global save_Sem_Status
    save_Sem_Status=sem_keep
    print("save sem is ",save_Sem_Status)
    
    if(request.method=='POST' and save_Sem_Status=='semster1' ):
        
        entry = sem1(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        database_commit(entry) #this fxn saves overhead below ifelse simply reduce no of lines
       
        return redirect("/getpapers")
        

    elif(request.method=='POST' and save_Sem_Status=='semster2' ):
        entry = sem2(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        database_commit(entry) #this fxn saves overhead below ifelse
        return redirect("/getpapers") 
    elif(request.method=='POST' and save_Sem_Status=='semster3' ):
        entry = sem3(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        database_commit(entry) #this fxn saves overhead below ifelse
        return redirect("/getpapers") 
    elif(request.method=='POST' and save_Sem_Status=='semster4' ):
        entry = sem4(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        database_commit(entry) #this fxn saves overhead below ifelse
        return redirect("/getpapers") 
    elif(request.method=='POST' and save_Sem_Status=='semster5' ):
        entry = sem5(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        database_commit(entry) #this fxn saves overhead below ifelse
        return redirect("/getpapers")   
    elif(request.method=='POST' and save_Sem_Status=='semster6' ):
        entry = sem6(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        database_commit(entry) #this fxn saves overhead below ifelse
        return redirect("/getpapers")    
    
    elif(request.method=='POST' and save_Sem_Status=='semster7' ):
        entry = sem7(batch=batch_get,papertype=papertype_get)
        db.session.add(entry)
        database_commit(entry) #this fxn saves overhead below ifelse
        return redirect("/getpapers") 
    elif(request.method=='POST' and save_Sem_Status=='semster8' ):
        entry = sem8(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        database_commit(entry) #this fxn saves overhead below ifelse
        return redirect("/getpapers") 
    
if __name__ == "__main__":
    app.run(debug=True,port=1125)    
