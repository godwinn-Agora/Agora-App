import os
import secrets
from PIL import Image
from flask import current_app
import re
import unicodedata


def slugify(text):
    # Normalise les accents
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    text = text.lower()
    text = re.sub(r'\s+', '-', text)         # remplace les espaces par des tirets
    text = re.sub(r'[^\w\-]', '', text)      # supprime les caractères spéciaux
    return text


def save_profile_picture(photo_file):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(photo_file.filename)
    filename = random_hex + f_ext
    path = os.path.join(current_app.root_path, 'static/profile_pics', filename)

    output_size = (300, 300)
    img = Image.open(photo_file)
    img.thumbnail(output_size)
    img.save(path)

    return filename
