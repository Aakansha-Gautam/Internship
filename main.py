
from flask import Flask,render_template,request,redirect
import flask
from datetime import datetime
from create_db import create_db
from boolean import boolean
from csv_add import csv_add
import os.path
from scrape import get_value
from daraz_scrape import get_value_daraz
import os
from downloading import access_file
from downlaoding_daraz import access_file_daraz
from files import files

app=Flask(__name__)

zip_path='C:\\Users\\aakan\\OneDrive\\Desktop\\flask'
path='C:\\Users\\aakan\\OneDrive\\Desktop\\flask\\files'

@app.route('/',methods=['GET','POST'])
def main():
    return (render_template('main.html'))

@app.route('/submit',methods=['POST'])
def upload():
    if request.method == 'POST':
        file=request.files['textfile']
        if file:
            file_name=str(datetime.now()).replace("-","_").replace(" ","_").replace(":","_").replace(".","_") 
            name,extension=file.filename.split(".")
            complete_name = os.path.join(path,name+file_name+".txt")   
            file.save(complete_name)
            create_db(complete_name)
        return (render_template('main.html',upload="upload successful"))
    else:
        return (render_template('main.html',upload="please upload your file"))


@app.route('/scrape',methods=['POST'])
def scrape():
    value=boolean()
    return (render_template('scrape.html',name=value))


@app.route('/scrape/google/<filename>/<id>')
def google_scraping(filename,id):
    get_value(filename,id)
    csv_add('google',id)
    return render_template('main.html')

@app.route('/scrape/daraz/<filename>/<id>')
def daraz_scraping(filename,id):
    get_value_daraz(filename,id)
    csv_add('daraz',id)
    return render_template('main.html')


@app.route('/download',methods=['POST'])
def download_value():
    scraped=files()
    return (render_template('download.html',name=scraped))

@app.route('/download/<id>',methods=['POST','GET'])
def downloading(id):
    access_file(id)
    zip_name=f"{id}.zip"
    return flask.send_from_directory(zip_path,zip_name,as_attachment=True)

# @app.route('/download/daraz/<id>',methods=['POST','GET'])
# def downloading_daraz(id):
#     access_file_daraz(id)
#     zip_name=f"{id}.zip"
#     return flask.send_from_directory(zip_path,zip_name,as_attachment=True)
    

if __name__=='__main__':
    app.run(debug=True)