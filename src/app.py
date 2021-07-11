# -*- coding: utf-8 -*-

import logging

from src import utils

logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("app").setLevel(logging.INFO)

file = 'fixtures/transactions/1'

def run():
    count = 0
    for line in utils.read_from_file_lines(file=file):
        count += 1
        print(line)

    print(count)
