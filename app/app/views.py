from werkzeug.utils import secure_filename
from app import app

import pandas as pd

import os

from flask import render_template,request,redirect,send_from_directory,flash,url_for

UPLOAD_FOLDER = os.getcwd()+"/uploads"
test = "./"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = "yeet"

@app.route("/",methods=['GET','POST'])
def index():
    print(test)
    if request.method == 'POST':
        
        print(request.files)
        if request.files:
            
            file = request.files["file"]
            filename = secure_filename(file.filename)
            print(file,filename)
            if file.filename =="":
                flash("No file selected")
                return redirect(request.url)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
            flash("File upload successful!")
            return redirect(request.url)
        else:
            print("Oops")
            return redirect(request.url)
            

    return render_template("public/index.html")

@app.route("/admin",methods=['GET','POST'])
def admin():
    if request.method == 'GET':
        print(request)
    return render_template("public/admin.html")

@app.route("/download",methods=['GET','POST'])
def dl(): 
    try:
        return send_from_directory(os.getcwd(), filename="after_rank.csv", as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.route("/eval",)
def runeval():
    file = open('/home/anant/ats-resumeparse/eval.py','r').read()
    exec(file)
    flash("Evaluation Complete!")
    return redirect(url_for('admin'))

@app.route("/rank",methods=['GET'])
def runrank():
    file = open('/home/anant/ats-resumeparse/rank.py','r').read()
    exec(file)
    flash("Ranking Completed Successfully! You can download results now.")
    return redirect(url_for('admin'))

@app.route("/results")
def results():
    table = pd.read_csv(os.path.join( os.getcwd(), 'after_rank.csv' ))
    return render_template("public/templates/empty.html", data=table.to_html())