from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField
from werkzeug.utils import secure_filename
import numpy as np
import pandas as pd
import psycopg2



#main 

from csv_import_functions import *

import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")

@app.route("/",methods=['GET','POST'])
@app.route("/home",methods=['GET','POST'])
def home():
    form=UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        
    
    return render_template("index.html",form=form)

if __name__=='__main__':
    app.run(debug=True)