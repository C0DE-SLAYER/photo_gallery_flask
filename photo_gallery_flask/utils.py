from photo_gallery_flask.models import metadata
from base64 import b64encode


def query_database():
    datas = metadata.query.all()
    decode_img = []
    for data in datas:
        img_base64 = b64encode(data.uploaded_img).decode("utf-8")
        decode_img.append(
            {
                "id": data.id,
                "title": data.title,
                "sub_title": data.sub_title,
                "category": data.category,
                "uploaded_img": img_base64,
            }
        )
    return decode_img


def getting_category():
    get_category = metadata.query.all()
    unique_category = list(
        set([get_category[i].category for i in range(len(get_category))])
    )
    try:
        unique_category.remove("")
    except:
        pass
    return unique_category
