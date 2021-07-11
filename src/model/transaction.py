# -*- coding: utf-8 -*-

from src.model import res

class Transactions:
    def __init__(self, data):
        self.transactions = Transactions.factory(data)

    @staticmethod
    def factory(data):
        result  = []
        for line in data:
            if len(line.split()) > 3:
                el = Transaction(line.split())
                result.append(el)
        return result

class Transaction:

    def __init__(self, data):
        self.object_id = data[0].strip()
        self.user_id = data[1].strip()
        self.time = f'{data[2]} {data[3]}'.strip()
        self.txt = ' '.join(data[4:])
        self.buy = False
        self.sell = False
        if 'купил' in self.txt:
            self.buy = True
        if 'продал' in self.txt:
            self.sell = True

        self.resource = res.Resource(data[0], data[4:])

    def __str__(self):
        return f'Transaction: objId:{self.object_id}, time:{self.time}. {self.resource}'

    def __repr__(self):
        return self.__str__()
