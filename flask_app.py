from flask import Flask, render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/upload")
def upload_papers():
    return render_template("upload.html")
@app.route("/about")
def About():
    return render_template("about.html")

@app.route("/getpapers")
def gwtpaper():
    return  render_template("getpapers.html")

#below fxn gets value from drop of semster in upload paper
@app.route("/paper_show" , methods=['GET', 'POST'])
def return_sem():
    select = request.form['sem']
    select = request.form.get('sem')
    #return(str(select)) # just to see what select is
    print("hey fetched val is ",str(select))
    return render_template('paper_show.html',param=str(select)) #param is parameter that i m passing to html page
if __name__ == "__main__":
    app.run(debug=True,port=1115)    
