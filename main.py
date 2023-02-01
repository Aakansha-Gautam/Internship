
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
from files import files
from api_files import create_db_api
from api_display import path_api
from update import update_val
from downlaoding_daraz import access_file_daraz
from api_final import getRecipeByIngredients
from extract_files import files_extract
from api_download import access_file_api
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

@app.route('/download/<id>/',methods=['POST','GET'])
def downloading(id):
    access_file(id)
    zip_name=f"{id}_google.zip"
    return flask.send_from_directory(zip_path,zip_name,as_attachment=True)

@app.route('/download/<id>',methods=['POST','GET'])
def downloading_daraz(id):
    access_file_daraz(id)
    zip_name=f"{id}_daraz.zip"
    return flask.send_from_directory(zip_path,zip_name,as_attachment=True)

api_path="C:\\Users\\aakan\\OneDrive\\Desktop\\flask\\api_files"
@app.route('/api',methods=['GET','POST'])
def api_page():
    return render_template('api.html')

@app.route('/api/upload',methods=['GET','POST'])
def api_upload():
    if request.method == 'POST':
        file=request.files['textfile']
        if file:
            file_name=str(datetime.now()).replace("-","_").replace(" ","_").replace(":","_").replace(".","_") 
            name,extension=file.filename.split(".")
            complete_name = os.path.join(api_path,name+file_name+".txt")   
            file.save(complete_name)
            create_db_api(complete_name)
        return (render_template('api.html',upload="upload successful"))
    else:
        return (render_template('api.html',upload="please upload your file"))

@app.route('/api/process',methods=["POST"])
def display():
    value=path_api()
    return (render_template('display.html',name=value))

@app.route('/api/process/<filename>/<id>')
def processing(filename,id):
    getRecipeByIngredients(filename,id)
    update_val(id)
    return render_template('api.html')

@app.route('/download/api',methods=['POST'])
def download_value_api():
    value=files_extract()
    return (render_template('download_api.html',name=value))

@app.route('/download/api/<id>',methods=['POST','GET'])
def downloading_api(id):
    access_file_api(id)
    zip_name=f"{id}_api.zip"
    return flask.send_from_directory(zip_path,zip_name,as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)