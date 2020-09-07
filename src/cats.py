import requests
import logging
import tempfile
import webbrowser
import random


class Cats:
    http_code: int

    def __init__(self, http=None):
        self.__http_code = http

    def run(self):
        self.http_code = self.choose_code(self.http_code)
        if self.http_code != 0:
            self.download_cat_img()

    def download_cat_img(self):
        url = "https://http.cat/" + str(self.http_code) + ".jpg"
        img = requests.get(url)
        logging.debug("URL:" + {url})
        with open(tempfile.NamedTemporaryFile(suffix=".jpg").name, "wb") as file:
            file.write(img.content)
            webbrowser.open(file.name)

    def choose_code(self, http_code=None) -> int:
        http_codes_list = [100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402,
                           403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 420, 421, 422,
                           423, 424, 425, 426, 429, 431, 444, 450, 451, 499, 500, 501, 502, 503, 504, 506, 507, 508,
                           509, 510, 511, 599]
        http_code_out = 0
        if http_code is None:
            http_code_out = http_codes_list[random.randint(0, len(http_codes_list))]
            logging.warning(f'Random code selected: {http_code_out}')
        if http_code in http_codes_list:
            logging.debug(f'Selected: {http_code}')
            http_code_out = http_code
        else:
            logging.critical("Wrong code selected!")
        return http_code_out
