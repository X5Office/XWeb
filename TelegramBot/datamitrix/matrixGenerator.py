import string
import qrcode
import random
from io import BytesIO
from Core.config import DATAMATRIX_template
from telegram import InputMediaPhoto

def generateDataMatrix(GTIN, count):
    dm_template = DATAMATRIX_template

    dm_strings = []

    for _ in range(count):
        random_chars = ''.join(random.choices(string.ascii_lowercase, k=3))
        dm_string = dm_template.replace('+', GTIN).replace('===', random_chars)
        dm_strings.append(dm_string)

    qr_images = []
    for dm_string in dm_strings:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(dm_string)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        qr_images.append(img)

    media_group = []
    for i, img in enumerate(qr_images):
        bio = BytesIO()
        bio.name = f'qr_code_{i}.png'
        img.save(bio, 'PNG')
        bio.seek(0)
        media_group.append(InputMediaPhoto(bio))

    return media_group
