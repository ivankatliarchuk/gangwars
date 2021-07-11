# -*- coding: utf-8 -*-

import logging

from src import utils
from src.model import transaction

logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("app").setLevel(logging.INFO)

file = 'fixtures/transactions/1'

def run():
    tr = transaction.Transactions(utils.read_from_file_lines(file=file))
    for el in tr.transactions:
        print(el)
