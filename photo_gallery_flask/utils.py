from photo_gallery_flask.models import metadata
from photo_gallery_flask import db

def getting_category():
    get_category = db.session.query(metadata.category).distinct().all()
    unique_category = [category[0] for category in get_category]
    unique_category.remove('')
    return unique_category
