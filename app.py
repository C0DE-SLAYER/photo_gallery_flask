from flask import Flask, render_template, request
import json

app = Flask(__name__)
with open('photo_data.json','r') as f:
    photo_data = json.load(f)

index = [1, 2, 3, 4, 5, 6, 4, 7, 4, 7, 8, 7, 9,2,10,11,12,10,13]

@app.route('/')
def hello():
    return render_template('index.html',photo_data=photo_data,range_len=len(photo_data),index=index)

@app.route('/login', methods=['GET','POST'])
def login_page():
    if request.method == "GET":
        return render_template('login_page.html')
    else:
        email = request.form['email']
        passwd = request.form['passwd']
        return f"{email}  {passwd}"

if __name__ == '__main__':
    app.run(debug=True)