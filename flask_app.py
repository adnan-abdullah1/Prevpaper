from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy 
import pymysql
import sqlalchemy.dialects.sqlite
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///paper_database.db"#"mysql+pymyql://root:admin@127.0.0.1/btech"
db = SQLAlchemy(app)   #db object
class sem1(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    
    papertype = db.Column(db.String(120), nullable=True)
    paper = db.Column(db.BLOB, nullable=False)
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

db.create_all()

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
    #select = request.form['sem']
    select = request.form.get('sem')
    
    #makin this var global so i can use sem value in other fxns
    global sem_keep
    sem_keep=str(select) 
    radio_val = request.form['upload_download']
    radio_val=request.form.get('upload_download')
    if str(radio_val)=='upload':
        return render_template('uploadtemplate.html',param=str(select),param1=str(radio_val))
    elif str(radio_val=='download'):
        def fetch_db():
            print(select)
            if select=='semster1':
                return sem1.query.all()
            elif select=='semster2':
                return sem2.query.all()
            elif select=='semster3':
                return sem3.query.all()
            elif select=='semster4':
                return sem4.query.all()
            elif select=='semster4':
                return sem1.query.all()
            elif select=='semster5':
                return sem5.query.all()
            elif select=='semster6':
                return sem6.query.all()
            elif select=='semster7':
                return sem7.query.all()
            elif select=='semster8':
                return sem8.query.all()
            else:
                return "found nothing"
        data=fetch_db()
        
        return render_template('paper_show.html',param=data)
        

@app.route("/upload_papertodb" , methods=['GET', 'POST'])
def upload_papertodb():
    batch_get = request.form['batch']
    papertype_get = request.form['papertype'].upper()
    
    paper_file = request.files['paper'].read()#request.files['paper']
    global save_Sem_Status
    save_Sem_Status=sem_keep
    print("save sem is ",save_Sem_Status)
    if(request.method=='POST' and save_Sem_Status=='semster1' ):
        entry = sem1(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers")
    elif(request.method=='POST' and save_Sem_Status=='semster2' ):
        entry = sem2(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers") 
    elif(request.method=='POST' and save_Sem_Status=='semster3' ):
        entry = sem3(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers") 
    elif(request.method=='POST' and save_Sem_Status=='semster4' ):
        entry = sem4(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers") 
    elif(request.method=='POST' and save_Sem_Status=='semster5' ):
        entry = sem5(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers")   
    elif(request.method=='POST' and save_Sem_Status=='semster6' ):
        entry = sem6(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers")    
    
    elif(request.method=='POST' and save_Sem_Status=='semster7' ):
        entry = sem7(batch=batch_get,papertype=papertype_get)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers") 
    elif(request.method=='POST' and save_Sem_Status=='semster8' ):
        entry = sem8(batch=batch_get,papertype=papertype_get,paper=paper_file)
        db.session.add(entry)
        db.session.commit()
        return redirect("/getpapers") 
    else:
        return render_template("uploadtemplatte.html")
if __name__ == "__main__":
    app.run(debug=True,port=1125)    
