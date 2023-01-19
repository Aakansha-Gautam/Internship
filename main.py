
from flask import Flask,render_template,request,redirect
from datetime import datetime
import create_db,boolean,csv_add,unscraped
import os.path
from scrape import get_value
import os

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/submit',methods=['POST'])
def upload():
    if request.method == 'POST':
        file=request.files['textfile']
        if file:
            file_name=str(datetime.now()).replace("-","_").replace(" ","_").replace(":","_").replace(".","_") 
            name,extension=file.filename.split(".")
            complete_name = os.path.join(name,file_name+".txt")   
            file.save(complete_name)
            create_db(complete_name)
            unscraped_files = unscraped()
        return (render_template('scrape.html',unscraped_files=unscraped_files))
    else:
        return (render_template('scrape.html'))
        # return(render_template('form.html',uplaod='file uploaded'))

@app.route('/scrape',methods=['POST'])
def scrape():
    value=boolean()
    file_path=value[0]
    id=value[1]
    with open(file_path, "r") as myfile:
        line  = myfile.readline().strip()
        get_value(line,id,file_path)
        csv_add(line,id)
    return(render_template('form.html',scrape='Scraped and table creation'))

# @app.route('/database',methods=['POST'])
# def to_database():
#     value=boolean()
#     file_path=value[0]
#     database(f'{file_path}.csv')
#     return(render_template('form.html',database='Inserted into database'))

    

if __name__=='__main__':
    app.run(debug=True)