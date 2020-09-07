import logging
import argparse
import sys
from src.cats import Cats


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.getLogger('urllib3').setLevel(logging.CRITICAL)
    parser = argparse.ArgumentParser(
        description="./httpcat.py a program to get cat picture for a http status")
    parser.add_argument('-s', '--status', type=int, nargs='?',
                        help="specify http status to get")
    cat = Cats(parser.parse_args(sys.argv[1:]).status)
    cat.run()


