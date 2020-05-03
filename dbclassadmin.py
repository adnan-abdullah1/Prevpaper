
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask

app=Flask(__name__)
jb = SQLAlchemy(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///admin.db"#"mysql+pymyql://root:admin@127.0.0.1/btech"
  #db object
app.secret_key = '#@asdf_!!!..3'
#sjb.create_all()
class admin(jb.Model):
    sno = jb.Column(jb.Integer, primary_key=True)
    username = jb.Column(jb.String(120), nullable=False)
    password=jb.Column(jb.String(120), nullable=False)
    
    def __repr__(self):
        return 'data is : ' + str(self.sno)
