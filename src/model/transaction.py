# -*- coding: utf-8 -*-

from src.model import res, constants as cs


class Transactions:
    def __init__(self, data):
        self.resources = {
            cs.Res.TRAVA: {
                'buy': {
                    'total': 0,
                    'cost': set()
                },
                'sell': {
                    'total': 0,
                    'cost': set()
                }
            },
            cs.Res.BOXITY: {
                'buy': {
                    'total': 0,
                    'cost': set()
                },
                'sell': {
                    'total': 0,
                    'cost': set()
                }
            },
            cs.Res.URAN: {
                'buy': {
                    'total': 0,
                    'cost': set()
                },
                'sell': {
                    'total': 0,
                    'cost': set()
                }
            },
            cs.Res.MAK: {
                'buy': {
                    'total': 0,
                    'cost': set()
                },
                'sell': {
                    'total': 0,
                    'cost': set()
                }
            },
            cs.Res.STAL: {
                'buy': {
                    'total': 0,
                    'cost': set()
                },
                'sell': {
                    'total': 0,
                    'cost': set()
                }
            },
            cs.Res.ALUMINII: {
                'buy': {
                    'total': 0,
                    'cost': set()
                },
                'sell': {
                    'total': 0,
                    'cost': set()
                }
            },
        }
        self.transactions = self.factory(data)

    def factory(self, data):
        result  = []
        for line in data:
            if len(line.split()) > 3:
                el = Transaction(line.split())
                type = el.resource.type
                if type in self.resources:
                    res = self.resources[type]
                    if el.resource.buy:
                        res['buy']['total'] += el.resource.total
                        res['buy']['cost'].add(el.resource.cost)
                    elif el.resource.sell:
                        res['sell']['total'] += el.resource.total
                        res['sell']['cost'].add(el.resource.cost)
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
