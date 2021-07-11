# -*- coding: utf-8 -*-

from src.model import res, constants as cs


class Transactions:
    def __init__(self, data):
        self.resources = {
            cs.Res.TRAVA: {
                'buy': {
                    'total': 0
                },
                'sell': {
                    'total': 0
                }
            },
            cs.Res.BOXITY: {
                'buy': {
                    'total': 0
                },
                'sell': {
                    'total': 0
                }
            },
            cs.Res.URAN: {
                'buy': {
                    'total': 0
                },
                'sell': {
                    'total': 0
                }
            },
            cs.Res.MAK: {
                'buy': {
                    'total': 0
                },
                'sell': {
                    'total': 0
                }
            },
            cs.Res.STAL: {
                'buy': {
                    'total': 0
                },
                'sell': {
                    'total': 0
                }
            },
            cs.Res.ALUMINII: {
                'buy': {
                    'total': 0
                },
                'sell': {
                    'total': 0
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
                        action = res['buy']['total']
                        res['buy']['total'] = action + el.resource.total
                    elif el.resource.sell:
                        action = res['sell']['total']
                        res['sell']['total'] = action + el.resource.total
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
