import urllib.parse

def text_codec(text):
    encoded_bytes = text.encode('utf-8')
    encoded_text = urllib.parse.quote(encoded_bytes, safe='')
    return encoded_text