import time
from urllib.parse import urlencode

from curl_cffi import requests

def search_locality(text: str):
    r = requests.get("https://pkk.rosreestr.ru/api/typeahead/1", params={"text": text, "_": int(time.time()*1000)}, impersonate="chrome110", verify="russian_trusted_root_ca.cer")
    print(r.text)

search_locality("пиголи")