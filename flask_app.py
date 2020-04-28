from flask import Flask, render_template,request,redirect,request
from flask_sqlalchemy import SQLAlchemy 
from flask import send_file  
import sqlalchemy.dialects.sqlite
from flask import flash
import time
from io import BytesIO
app=Flask(__name__)
app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///paper_database.db"#"mysql+pymyql://root:admin@127.0.0.1/btech"
db = SQLAlchemy(app)   #db object

class sem1(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    paper_ext=db.Column(db.String(120), nullable=True)
    papertype = db.Column(db.String(120), nullable=True)
    subject=db.Column(db.String(120), nullable=True)
    paper = db.Column(db.BLOB, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem2(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    paper_ext=db.Column(db.String(120), nullable=True)
    papertype = db.Column(db.String(120), nullable=True)
    subject=db.Column(db.String(120), nullable=True)
    paper = db.Column(db.BLOB, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
   
class sem3(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    paper_ext=db.Column(db.String(120), nullable=True)
    papertype = db.Column(db.Integer, nullable=True)
    subject=db.Column(db.String(120), nullable=True)
    paper = db.Column(db.BLOB, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem4(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    paper_ext=db.Column(db.String(120), nullable=True)
    papertype = db.Column(db.String(120), nullable=True)
    subject=db.Column(db.String(120), nullable=True)
    paper = db.Column(db.BLOB, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem5(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    paper_ext=db.Column(db.String(120), nullable=True)
    papertype = db.Column(db.String(120), nullable=True)
    subject=db.Column(db.String(120), nullable=True)
    paper = db.Column(db.BLOB, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem6(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    paper_ext=db.Column(db.String(120), nullable=True)
    papertype = db.Column(db.String(120), nullable=True)
    subject=db.Column(db.String(120), nullable=True)
    paper = db.Column(db.BLOB, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)

class sem7(db.Model):

    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    paper_ext=db.Column(db.String(120), nullable=True)
    paper_ext=db.Column(db.String(120), nullable=True)
    papertype = db.Column(db.String(120), nullable=True)
    subject=db.Column(db.String(120), nullable=True)
    paper = db.Column(db.BLOB, nullable=False)
    def __repr__(self):
        return 'data is : ' + str(self.sno)
class sem8(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=True)
    paper_ext=db.Column(db.String(120), nullable=True)
    papertype = db.Column(db.String(120), nullable=True)
    subject=db.Column(db.String(120), nullable=True)
    paper = db.Column(db.BLOB, nullable=False)
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
def getpaper():

    return  render_template("upload_download.html",param_btn="get-papers",param="Download your papers make selection appropriately")
@app.route("/download_paper")
def download_paper():
    if request.form.get('Download')=="Download":
        print("lovvvvvvvvvvv")
        return "i am working"
    else:
        print(" i am not getting button response")
        return " not working button" 
    #print("hyyyy",request.form['Download'])
    
    if __sem_keep=='semster1' and 'Download' in request.form:    
        print(" sem one bro ")                
        return send_file(BytesIO(sem1.query.all()[1].paper),
        attachment_filename=sem1.query.all()[1].paper_ext,as_attachment="True")
    
    """

    elif __sem_keep=='semster2':                             
        return send_file(BytesIO(sem2.query.all()[0].paper),
        attachment_filename=sem2.query.all()[0].paper_ext,as_attachment="True")
    elif __sem_keep=='semster3': 
        print(" sem3is selected")                            
        return send_file(BytesIO(sem3.query.all()[0].paper),
        attachment_filename=sem3.query.all()[0].paper_ext,as_attachment="True")
    elif __sem_keep=='semster4':  
        print(" i am selected ")                           
        return send_file(BytesIO(sem4.query.all()[3].paper),
        attachment_filename=sem4.query.all()[3].paper_ext,as_attachment="True")
    elif __sem_keep=='semster5':                             
        return send_file(BytesIO(sem5.query.all()[0].paper),
        attachment_filename=sem5.query.all()[0].paper_ext,as_attachment="True")
    elif __sem_keep=='semster6':                             
        return send_file(BytesIO(sem6.query.all()[0].paper),
        attachment_filename=sem6.query.all()[0].paper_ext,as_attachment="True")
    elif __sem_keep=='semster7':                             
        return send_file(BytesIO(sem7.query.all()[0].paper),
        attachment_filename=sem7.query.all()[0].paper_ext,as_attachment="True")
    elif __sem_keep=='semster8':                             
        return send_file(BytesIO(sem8.query.all()[0].paper),
        attachment_filename=sem8.query.all()[0].paper_ext,as_attachment="True")
    

    """        
       

#below fxn gets value from drop of semster in upload paper
@app.route("/fetch_sem_upload_download" , methods=['GET','POST'])
def return_sem():
    #select = request.form['sem']
    select = request.form.get('sem')
    
    #makin this var global so i can use sem value in other fxns
    global __sem_keep
    __sem_keep=str(select) 
    radio_val = request.form['upload_download']
    radio_val=request.form.get('upload_download')
    if str(radio_val)=='upload':
        
        return render_template('uploadtemplate.html',param=str(select),param1=str(radio_val))
    elif str(radio_val=='download'):
        def fetch_db():
            
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
    print("paper type ",papertype_get)
    subject_get=request.form['subject'].upper()
    paper_file = request.files['paper'].read()#request.files['paper']
    paper_ext = str(request.files['paper']) #gets file name
    paper_ext=paper_ext.split()[1] #getting filename from form 
    #paper_ext=str(paper_ext)


    def internal_lines(get_list):
        if len(get_list)==0:
            #database is empty here
            return "can_upload"
        else:
            for i in get_list:
                print("sub is ",i.subject)
                if subject_get==i.subject:
                    search="cant_upload"
                    break
                elif subject_get!=i.subject:
                    search="can_upload"
            return search
    #paper_ext will save filename with extension into database
    def search_db_forduplcate(): 
        # search_db_forduplcate()--> internal_lines()
        # can_upload or cant_upload <-- return seacrh 
        # this function will search datbase for dublicate
        if __sem_keep=="semster1":
            search_list_sem1=sem1.query.all()
            search_saved=internal_lines(search_list_sem1)
            return search_saved
        elif  __sem_keep=="semster2":
            search_list_sem2=sem2.query.all()
            search_saved=internal_lines(search_list_sem2)
            return search_saved
        elif  __sem_keep=="semster3":
            search_list_sem3=sem3.query.all()
            search_saved=internal_lines(search_list_sem3)
            return search_saved
        elif  __sem_keep=="semster4":
            search_list_sem4=sem4.query.all()
            search_saved=internal_lines(search_list_sem4)
            return search_saved
        elif  __sem_keep=="semster5":
            search_list_sem5=sem5.query.all()
            search_saved=internal_lines(search_list_sem5)
            return search_saved
        elif  __sem_keep=="semster6":
            search_list_sem6=sem6.query.all()
            search_saved=internal_lines(search_list_sem6)
            return search_saved
        elif  __sem_keep=="semster7":
            search_list_sem7=sem7.query.all()
            search_saved=internal_lines(search_list_sem7)
            return search_saved
        elif  __sem_keep=="semster8":
            search_list_sem8=sem8.query.all()
            search_saved=internal_lines(search_list_sem8)
            return search_saved


    if(request.method=='POST' and __sem_keep=='semster1'):
        return_search=search_db_forduplcate()
        if return_search=="can_upload":
            entry = sem1(batch=batch_get,paper_ext=paper_ext,papertype=papertype_get,subject=subject_get,paper=paper_file)
            db.session.add(entry)
            db.session.commit()
            return redirect("/getpapers")
        else:
            flash(" Paper already exists ")
            return redirect("/")
        
    elif(request.method=='POST' and __sem_keep=='semster2' ):
        return_search=search_db_forduplcate()
        if return_search=="can_upload":
            entry = sem2(batch=batch_get,paper_ext=paper_ext,papertype=papertype_get,subject=subject_get,paper=paper_file)
            db.session.add(entry)
            db.session.commit()
            return redirect("/getpapers") 
        else:
            flash(" Paper already exists ")
            return redirect("/")
    elif(request.method=='POST' and __sem_keep=='semster3' ):
        return_search=search_db_forduplcate()
        if return_search=="can_upload":
            entry = sem3(batch=batch_get,paper_ext=paper_ext,papertype=papertype_get,subject=subject_get,paper=paper_file)
            db.session.add(entry)
            db.session.commit()
            return redirect("/getpapers")
        else:
            flash(" Paper already exists ")
            return redirect("/") 
    elif(request.method=='POST' and __sem_keep=='semster4' ):
        return_search=search_db_forduplcate()
        if return_search=="can_upload":
            entry = sem4(batch=batch_get,paper_ext=paper_ext,papertype=papertype_get,subject=subject_get,paper=paper_file)
            db.session.add(entry)
            db.session.commit()
            return redirect("/getpapers") 
        else:
            flash(" Paper already exists ")
            return redirect("/")
    elif(request.method=='POST' and __sem_keep=='semster5' ):
        return_search=search_db_forduplcate()
        if return_search=="can_upload":
            entry = sem5(batch=batch_get,paper_ext=paper_ext,papertype=papertype_get,subject=subject_get,paper=paper_file)
            db.session.add(entry)
            db.session.commit()
            return redirect("/getpapers")
        else:
            flash(" Paper already exists ")
            return redirect("/")   
    elif(request.method=='POST' and __sem_keep=='semster6' ):
        return_search=search_db_forduplcate()
        if return_search=="can_upload":
            entry = sem6(batch=batch_get,paper_ext=paper_ext,papertype=papertype_get,subject=subject_get,paper=paper_file)
            db.session.add(entry)
            db.session.commit()
            return redirect("/getpapers")    
        else:
            flash(" Paper already exists ")
            return redirect("/")
    elif(request.method=='POST' and __sem_keep=='semster7' ):
        return_search=search_db_forduplcate()
        if return_search=="can_upload":
            entry = sem7(batch=batch_get,paper_ext=paper_ext,papertype=papertype_get,subject=subject_get,paper=paper_file)
            db.session.add(entry)
            db.session.commit()
            return redirect("/getpapers") 
        else:
            flash(" Paper already exists ")
            return redirect("/")
    elif(request.method=='POST' and __sem_keep=='semster8' ):
        return_search=search_db_forduplcate()
        if return_search=="can_upload":
            entry = sem8(batch=batch_get,paper_ext=paper_ext,papertype=papertype_get,subject=subject_get,paper=paper_file)
            db.session.add(entry)
            db.session.commit()
            return redirect("/getpapers")
        else:
            flash(" Paper already exists ")
            return redirect("/") 
    else:
        return render_template("uploadtemplatte.html")
if __name__ == "__main__":
    app.run(debug=True,port=3000)    
        
    
