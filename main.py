from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/portofolio")
def portofolio():
    return render_template("portofolio.html")

@app.route("/portofolio/fakebook")
def fakebook():
    return render_template("fakebook.html")

@app.route("/portofolio/boogle")
def boogle():
    return render_template("boogle.html")

@app.route("/portofolio/hairsalon")
def hairsalon():
    return render_template("hairsalon.html")

if __name__== "__main__":
    app.run(port="5001")