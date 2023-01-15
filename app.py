from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
app.config['SECRET_KEY'] = 'thisissecretkey'
db = SQLAlchemy(app)

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


with open('photo_data.json','r') as f:
    photo_data = json.load(f)

index = [1, 2, 3, 4, 5, 6, 4, 7, 4, 7, 8, 7, 9,2,10,11,12,10,13]

@app.route('/')
def home():
    return render_template('index.html',photo_data=photo_data,range_len=len(photo_data),index=index)

@app.route('/dashboard')
# @login_required
def dashboard():
    return render_template('dashboard.html')


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


@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/update')
def update():
    return render_template('update.html')

if __name__ == '__main__':
    app.run(debug=True,host='192.168.0.107')