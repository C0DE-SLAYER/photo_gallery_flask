from photo_gallery_flask import app, db, login_manager
from photo_gallery_flask.models import User, metadata
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
import io
from werkzeug.security import check_password_hash
from PIL import Image
import base64


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

index = [1, 2, 3, 4, 5, 6, 4, 7, 4, 7, 8, 7, 9,2,10,11,12,10,13]

def query_database():
    metadata_db = metadata.query.all()
    decode_img = []
    for m in metadata_db:
        data = metadata(id=m.id,title=m.title,sub_title=m.sub_title,category=m.category,uploaded_img=base64.b64encode(m.uploaded_img).decode('utf-8'))
        decode_img.append(data)
    return decode_img

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
        username = request.form['username']
        passwd = request.form['passwd']
        user = User.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password,passwd):
                login_user(user)
                flash('Your Are Logged In Successfully')
                return redirect(url_for('dashboard'))
            else:
                flash('Please check your username or Check password is correct or not')
                return redirect(url_for('login'))
        else:
            flash('Please check your username or Check password is correct or not')
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
        category  = request.form['category'] if new_category == '' else new_category.replace(' ','_')
        upload_file = request.files['upload_img'].read()
        if upload_file:
            try:
                img = Image.open(io.BytesIO(upload_file))
                optimize_img = io.BytesIO()
                img.save(optimize_img , "webp", quality=50, optimize=True)
                optimize_img_data = optimize_img.getvalue()
                data_to_put_in_database = metadata(title=title,sub_title=sub_title,category=category,uploaded_img=optimize_img_data)
                db.session.add(data_to_put_in_database)
                db.session.commit()
                flash('Photo Uploaded Successfully')
                return redirect(url_for('upload'))
            except Exception as e:
                return f'{e}'
                flash(f'The photo was not uploaded. Try again')
                return redirect(url_for('upload'))
        else:
            flash(f'Please select correct file')
            return redirect(url_for('upload'))

@app.route('/update',methods=['POST'])
def update():
    title = request.form['title']
    sub_title = request.form['sub_title']
    category = request.form['category']
    id = request.form['ikivalue']
    photo_data = metadata.query.get(id)
    upload_file = request.files['file'].read()
    try:
        if upload_file:
            img = Image.open(io.BytesIO(upload_file))
            optimize_img = io.BytesIO()
            img.save(optimize_img , "webp", quality=50, optimize=True)
            optimize_img_data = optimize_img.getvalue()
        metadata.query.filter_by(id=id).update(dict(title=title if title else photo_data.title,sub_title=sub_title if sub_title else photo_data.sub_title,category=category if category else photo_data.category, uploaded_img= optimize_img_data if upload_file else photo_data.uploaded_img))
        db.session.commit()
        flash('Detail Updated')
        return redirect(url_for('dashboard'))
    except:
        flash('There was some error while changing the detail. Try again')
        return redirect(url_for('dashboard'))


@app.route('/delete',methods=['POST'])
def delete():
    id = request.form['ikivalue']
    delete_data = metadata.query.filter_by(id=id).first()
    db.session.delete(delete_data)
    db.session.commit()
    flash('The Selected Photo Has Been Deleted!')
    return redirect(url_for('dashboard'))


@app.route('/delete-category',methods=['POST'])
def delete_category():
    delete_category = request.form['category']
    metadata.query.filter_by(category=delete_category).update(dict(category=''))
    db.session.commit()
    flash(f'{delete_category} delete successfully')
    return redirect('dashboard')
