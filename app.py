from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meta_data.db'
app.config['SECRET_KEY'] = 'thisissecretkey'
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = 'static/img/test_photo'

app.app_context().push()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

class metadata(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    sub_title = db.Column(db.String(100))
    category = db.Column(db.String(100))
    photo_path = db.Column(db.String(500))


with open('photo_data.json','r') as f:
    photo_data = json.load(f)

index = [1, 2, 3, 4, 5, 6, 4, 7, 4, 7, 8, 7, 9,2,10,11,12,10,13]

def getting_category():
    get_category = metadata.query.all()
    unique_category = set([get_category[i].category for i in range(len(get_category))])
    if len(unique_category) == 0:
        unique_category = '0'
    return unique_category
    

@app.route('/')
def home():
    return render_template('index.html',photo_data=photo_data,range_len=len(photo_data),index=index)

@app.route('/dashboard')
# @login_required
def dashboard():
    metadata_query = metadata.query.all()
    return render_template('dashboard.html',photo_data=metadata_query,range_len=len(metadata_query),catergory=getting_category(),category_len=len(getting_category()))


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login_page.html')
    else:
        email = request.form['email']
        passwd = request.form['passwd']
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password,passwd):
                login_user(user)
                return redirect(url_for('dashboard'))
        else:
            flash('Please check your email or Check password is correct or not')
            return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html',catergory=getting_category() )
    else:
        title = request.form['title']
        sub_title = request.form['sub_title']
        new_category = request.form['new_category']
        category  = request.form['category'] if new_category == '' else new_category
        upload_file = request.files.getlist('upload_img')
        for file in upload_file:
            try:
                path = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
                file.save(path)
            except :
                flash(f'The photo was not uploaded. Try again')
                return redirect(url_for('upload'))
        data_to_put_in_database = metadata(title=title,sub_title=sub_title,category=category,photo_path=path.replace('static/',''))
        db.session.add(data_to_put_in_database)
        db.session.commit()
        flash('Photo Updated Successfully')
        return redirect(url_for('upload'))


@app.route('/update',methods=['POST'])
def update():
    if request.method == 'POST':


        title = request.form['title']
        sub_title = request.form['sub_title']
        category = request.form['category']
        id = request.form['ikivalue']       
        photo_data = metadata.query.filter_by(id=id)
        try:
            path = request.files['file']
            path1 = os.path.join(app.config['UPLOAD_FOLDER'],path.filename)
            path.save(path1) 
        except FileNotFoundError:
            pass

        metadata.query.filter_by(id=id).update(dict(title=title if title !='' else photo_data[0].title,sub_title=sub_title if sub_title !='' else photo_data[0].sub_title,category=category if category !='' else photo_data[0].category,photo_path=path1 if path !='' else photo_data[0].photo_path))
        db.session.commit()

        return redirect(url_for('dashboard'))
        
@app.route('/delete',methods=['POST'])
def delete():
    if request.method == 'POST':
        id = request.form['ikivalue']
        

if __name__ == '__main__':
    app.run(debug=True,host='172.25.171.70')