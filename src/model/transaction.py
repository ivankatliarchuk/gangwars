# -*- coding: utf-8 -*-

from src.model import res, constants as cs, cost


class Transactions:
    def __init__(self, data):
        self.resources = {
            cs.Res.TRAVA: {
                'buy': cost.Cost('buy', cs.Res.TRAVA),
                'sell': cost.Cost('sell', cs.Res.TRAVA),
                'diff': 0
            },
            cs.Res.BOXITY: {
                'buy': cost.Cost('buy', cs.Res.BOXITY),
                'sell': cost.Cost('sell', cs.Res.BOXITY),
                'diff': 0
            },
            cs.Res.URAN: {
                'buy': cost.Cost('buy', cs.Res.URAN),
                'sell': cost.Cost('sell', cs.Res.URAN),
                'diff': 0
            },
            cs.Res.MAK: {
                'buy': cost.Cost('buy', cs.Res.MAK),
                'sell': cost.Cost('sell', cs.Res.MAK),
                'diff': 0
            },
            cs.Res.STAL: {
                'buy': cost.Cost('buy', cs.Res.STAL),
                'sell': cost.Cost('sell', cs.Res.STAL),
                'diff': 0
            },
            cs.Res.ALUMINII: {
                'buy': cost.Cost('buy', cs.Res.ALUMINII),
                'sell': cost.Cost('sell', cs.Res.ALUMINII),
                'diff': 0
            },
            cs.Res.GANJIUM: {
                'buy': cost.Cost('buy', cs.Res.ALUMINII),
                'sell': cost.Cost('sell', cs.Res.ALUMINII),
                'diff': 0
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
                        res['buy'].add(el.resource.total, el.resource.cost)
                        res['diff'] -= el.resource.total
                    elif el.resource.sell:
                        res['sell'].add(el.resource.total, el.resource.cost)
                        res['diff'] += el.resource.total
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
