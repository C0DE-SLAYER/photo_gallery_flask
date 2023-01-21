from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['UPLOAD_FOLDER']

	
@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('gd.html')
    else: 
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)