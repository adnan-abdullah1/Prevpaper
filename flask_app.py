from flask import render_template,request,redirect,request,url_for
from flask import send_file  
#import sqlalchemy.dialects.sqlite
from flask import flash
#from flask_table import Table, Col
from io import BytesIO
from dbclass import *

app.secret_key = 'super secret key'

db = SQLAlchemy(app)   #db object


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

@app.route("/download_paper/<int:sno>")
def download_paper(sno):
    __sem__=__sem_keep
    __sem__=eval(__sem__[0:3]+__sem__[7:8]) #turns eg semster1 to sem1
    return send_file(BytesIO(__sem__.query.all()[sno].paper),
    attachment_filename=__sem__.query.all()[sno].paper_ext,as_attachment="True")
        

    
    
@app.route("/paper_show")
def paper_show():
    #select = request.form['sem']
    return render_template("paper_show.html")

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
        savesem=select
        savesem=eval(savesem[0:3]+savesem[7:8])
        data=savesem.query.all()
        
        return render_template('paper_show.html',param=data)
        

@app.route("/upload_papertodb" , methods=['GET', 'POST'])
def upload_papertodb():
    batch_get = request.form['batch']
    papertype_get = request.form['papertype'].upper()
    subject_get=request.form['subject'].upper()
    paper_file = request.files['paper'].read()#request.files['paper']
    paper_ext = str(request.files['paper']) #gets file name
    paper_ext=paper_ext.split()[1] #getting filename from form  eg 'abc.pdf'
    #paper_ext=str(paper_ext)


    def internal_lines(get_list):
        if len(get_list)==0:
            #database is empty here
            return "can_upload"
        else:
            for i in get_list:
                print("sub is ",i.subject)
                if subject_get==i.subject and papertype_get==i.papertype:
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
        save_sem1=eval("__sem_keep")
        save_sem1=eval(save_sem1[0:3]+save_sem1[7:8])
        search_list_sem1=save_sem1.query.all()
        search_saved=internal_lines(search_list_sem1)
        return search_saved
      

    if(request.method=='POST'  ):
        save_sem=eval("__sem_keep")
        save_sem=eval(save_sem[0:3]+save_sem[7:8])
        print("save sem si",save_sem)
        return_search=search_db_forduplcate()
        if return_search=="can_upload":
            entry = save_sem(batch=batch_get,paper_ext=paper_ext,papertype=papertype_get,subject=subject_get,paper=paper_file)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for("upload_papers"))  
        else:
            flash(" Paper already exists ")
            return redirect("/")
   
    else:
        return render_template("uploadtemplatte.html")
if __name__ == "__main__":
    app.run(debug=True,port=3002)    
        
    
