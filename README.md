![Logo](https://raw.githubusercontent.com/C0DE-SLAYER/photo_gallery_flask/master/photo_gallery_flask/static/github_img/logo.png)

> A simple Content Management System(CMS) for adding, deleting, editing photo in a gallery using flask

## About Flask
* Flask is a lightweight and flexible web framework for Python.
* It follows the WSGI standard and is compatible with various web servers.
* Flask's modular design allows for easy integration of extensions to enhance functionality.

## Installation

```python
git clone https://github.com/C0DE-SLAYER/photo_gallery_flask
cd photo_gallery_flask
pip install -r requirement.txt
python run.py
```

## For deployment instructions
- please visit the [deployment branch](https://github.com/C0DE-SLAYER/photo_gallery_flask/tree/deployment).


## Usage/Examples

1. Rename the .env.example file to .env. Sign in to [Supabase](https://supabase.com/), create a new project, and fill in the env variables with the values from your project.
2. Open a terminal and type for linux/mac `export FLASK_APP=photo_gallery_flask` and for windows type `set FLASK_APP=photo_gallery_flask`
3. Then type `flask shell` and type `db.create_all()` to create the db file use for the project 
4. Now to create the login detail run the following command in `flask shell`show in the images 
![demo_1](https://raw.githubusercontent.com/C0DE-SLAYER/photo_gallery_flask/master/photo_gallery_flask/static/github_img/user_command.png)
5. Once you have install all the requirement using pip and create the db. Run the app using `python run.py`
6. Now Head to your browser and type http://127.0.0.1:5000/ and http://127.0.0.1:5000/login head to login page and enter your username and password set in step 3.
7. Demo/Example : 
![demo_1](https://raw.githubusercontent.com/C0DE-SLAYER/photo_gallery_flask/master/photo_gallery_flask/static/github_img/demo_1.png)
![demo_2](https://raw.githubusercontent.com/C0DE-SLAYER/photo_gallery_flask/master/photo_gallery_flask/static/github_img/demo_2.png)
![demo_3](https://raw.githubusercontent.com/C0DE-SLAYER/photo_gallery_flask/master/photo_gallery_flask/static/github_img/demo_3.png)
![demo_4](https://raw.githubusercontent.com/C0DE-SLAYER/photo_gallery_flask/master/photo_gallery_flask/static/github_img/demo_4.png)

## License

[MIT](https://github.com/C0DE-SLAYER/photo_gallery_flask/blob/master/LICENSE.txt)