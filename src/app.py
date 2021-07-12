# -*- coding: utf-8 -*-

import logging
import glob
from datetime import datetime

from src import utils
from src.model import transaction

logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("app").setLevel(logging.INFO)

datetime_format = '%d.%m.%y %H:%M:%S'

folders = "fixtures/transactions/11-07-2021/*"

def run():
    from_date_str = '11.07.21 00:51:18'
    from_date = datetime.strptime(from_date_str, datetime_format)
    to_date_str = '11.07.21 23:44:16'
    to_date = datetime.strptime(to_date_str, datetime_format)

    lines = []

    for file in glob.glob(folders):
        for line in utils.read_from_file_lines(file=file):
            data = line.split()
            if len(data) >= 3:
                time = f'{data[2]} {data[3]}'.strip()
                current = datetime.strptime(time, datetime_format)
                if current > from_date and current < to_date:
                    lines.append(line)

    tr = transaction.Transactions(lines)
    print ("{:<20} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('Type','Buy.Total', 'Sell.Total', 'Balance', 'Buy.Cost','Sell.Cost', 'Experience'))

    total_balance = 0
    total_experience = 0

    for e in tr.resources:
        print ("{:<20} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(e, tr.resources[e]['buy'].total, tr.resources[e]['sell'].total, tr.resources[e]['diff'], tr.resources[e]['buy'].cost(), tr.resources[e]['sell'].cost(), tr.resources[e]['sell'].experience))
        total_balance += tr.resources[e]['diff']
        total_experience += tr.resources[e]['sell'].experience

    print(f'Total Balance: {total_balance}')
    print(f'Total Balance: {total_experience}')
