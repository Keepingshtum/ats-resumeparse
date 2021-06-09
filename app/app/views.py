from werkzeug.utils import secure_filename
from app import app

import os

from flask import render_template,request,redirect,flash

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
                print("No file selected")
                return redirect(request.url)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
            return redirect(request.url)
        else:
            print("Oops")
            return redirect(request.url)
            

    return render_template("public/index.html")

@app.route("/about")
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """