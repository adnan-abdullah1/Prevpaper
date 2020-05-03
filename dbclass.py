
from flask_sqlalchemy import SQLAlchemy 

from flask import Flask

app=Flask(__name__)
db = SQLAlchemy(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///paper_database.db"#"mysql+pymyql://root:admin@127.0.0.1/btech"
  #db object
app.secret_key = '#@asdf_!!!..3'
#db.create_all()
"""
####admin login######
class admin(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    password=db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return 'data is : ' + str(self.sno)
"""
#semster database #######
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

