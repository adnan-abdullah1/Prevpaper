from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/contact")
def select_course():
    return render_template("contact.html")
@app.route("/about")
def About():
    return render_template("about.html")


app.run(debug=True,port=50)