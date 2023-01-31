from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from werkzeug.security import check_password_hash
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



index = [1, 2, 3, 4, 5, 6, 4, 7, 4, 7, 8, 7, 9,2,10,11,12,10,13]

def query_database():
    return metadata.query.all()


def getting_category():
    get_category = query_database()
    unique_category = list(set([get_category[i].category for i in range(len(get_category))]))
    try: 
        unique_category.remove('')
    except:
        pass
    return unique_category

@app.route('/')
def home():
    metadata_query = query_database()
    return render_template('index.html',photo_data=metadata_query,range_len=len(metadata_query),index=index,catergory=getting_category())

@app.route('/dashboard')
@login_required
def dashboard():
    metadata_query = query_database()
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
                flash('Your Are Logged In Successfully')
                return redirect(url_for('dashboard'))
            else:
                flash('Please check your email or Check password is correct or not')
                return redirect(url_for('login'))
        else:
            flash('Please check your email or Check password is correct or not')
            return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You Are Logged Out Successfully')
    return redirect('/')


@app.route('/upload', methods=['GET','POST'])
@login_required
def upload():
    if request.method == 'GET':
        return render_template('upload.html',catergory=getting_category())
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
        path = request.files['file']
        if path.filename != '':
            path1 = os.path.join(app.config['UPLOAD_FOLDER'],path.filename)
            path.save(path1)
            os.remove(f'static/{photo_data[0].photo_path}')

        metadata.query.filter_by(id=id).update(dict(title=title if title !='' else photo_data[0].title,sub_title=sub_title if sub_title !='' else photo_data[0].sub_title,category=category if category !='' else photo_data[0].category,
        photo_path=path1.replace('static/','') if path.filename != '' else photo_data[0].photo_path))
        db.session.commit()
        flash('Detail Updated')
        return redirect(url_for('dashboard'))
        
@app.route('/delete',methods=['POST'])
def delete():
    if request.method == 'POST':
        id = request.form['ikivalue']
        delete_data = metadata.query.filter_by(id=id).first()
        try:
            os.remove(f'static/{delete_data.photo_path}')
        except :
            pass
        db.session.delete(delete_data)
        db.session.commit()
        flash('The Selected Photo Has Been Deleted!')
        return redirect(url_for('dashboard'))


@app.route('/delete-category',methods=['POST'])
def delete_category():
    if request.method == 'POST':
        delete_category = request.form['category']
        metadata.query.filter_by(category=delete_category).update(dict(category=''))
        db.session.commit()
        flash(f'{delete_category} delete successfully')
        return redirect('dashboard')


if __name__ == '__main__':
    app.run(debug=True,host='192.168.0.113')