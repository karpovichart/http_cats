import requests
import os
import sys
import argparse
import random


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="./httpcat.py a program to get cat picture for a http status")
    parser.add_argument('-s', '--status', type=int, nargs='?', help="specify http status to get")
    return parser


def download_cat_img(http_code: int) -> None:
    print(http_code)
    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    url = "https://http.cat/" + str(http_code) + ".jpg"
    path = "tmp\\" + str(http_code) + ".jpg"
    img = requests.get(url)
    out = open(path, "wb")
    out.write(img.content)
    out.close()
    os.startfile(path)
    return None


def run() -> None:
    http_codes_list = [100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402,
                       403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 420, 421, 422,
                       423, 424, 425, 426, 429, 431, 444, 450, 451, 499, 500, 501, 502, 503, 504, 506, 507, 508,
                       509, 510, 511, 599]
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.status is None:
        http_code = http_codes_list[random.randint(0, len(http_codes_list))]
        download_cat_img(http_code)
        return None

    if namespace.status in http_codes_list:
        print("Complete.")
        download_cat_img(namespace.status)
    else:
        print("Bad Code!")
    return None


if __name__ == '__main__':
    run()