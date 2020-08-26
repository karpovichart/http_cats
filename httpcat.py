import requests
import os
import sys
from sys import platform
import argparse
import random
import logging

'''
warnings - no parametrs
debug level - what params
debug level - what url will be download

'''


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="./httpcat.py a program to get cat picture for a http status")
    parser.add_argument('-s', '--status', type=int, nargs='?', help="specify http status to get")
    return parser


def choose_os() -> str:
    if platform == "win32":
        return "\\"
    return "/"


def download_cat_img(http_code: int) -> None:
    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    url = "https://http.cat/" + str(http_code) + ".jpg"
    path = "tmp" + choose_os() + str(http_code) + ".jpg"
    img = requests.get(url)
    logging.debug(f'URL: {url}')
    with open(path, "wb") as file:
        file.write(img.content)
    os.startfile(path)
    return None


def choose_code(code: int) -> int:
    http_codes_list = [100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402,
                       403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 420, 421, 422,
                       423, 424, 425, 426, 429, 431, 444, 450, 451, 499, 500, 501, 502, 503, 504, 506, 507, 508,
                       509, 510, 511, 599]
    if code is None:
        http_code = http_codes_list[random.randint(0, len(http_codes_list))]
        logging.warning(f'Random code selected: {http_code}')
        return http_code
    if code in http_codes_list:
        logging.debug(f'Selected: {code}')

        return code
    else:
        logging.critical("Wrong code selected!")
        return 0


def run() -> None:
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    http_code = choose_code(namespace.status)

    if http_code != 0:
        download_cat_img(http_code)
    return None


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.getLogger('urllib3').setLevel(logging.CRITICAL)
    run()
