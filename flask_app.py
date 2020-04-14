from flask import Flask, render_template
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
if __name__ == "__main__":
    app.run(debug=True,port=1111)    
