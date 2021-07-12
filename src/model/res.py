# -*- coding: utf-8 -*-

from src.model import constants as cs

resources = [cs.Res.TRAVA, cs.Res.BOXITY, cs.Res.URAN, cs.Res.MAK, cs.Res.STAL, cs.Res.ALUMINII, cs.Res.GANJIUM]


class Resource:

    def __init__(self, object_id, data):
        self.object_id = object_id
        self.data = data
        self.txt = ' '.join(data)
        self.buy = False
        self.sell = False
        self.type = None

        for res in resources:
            if res.value in ' '.join(data):
                self.type = res

        self.count = -1
        self.total = -1
        self.cost = -1

        for el in data:
            index = data.index(el)
            if 'купил' == el:
                self.buy = True
                self.count = data[index + 1]
            elif 'продал' == el:
                self.sell = True
                self.count = data[index + 1]
            elif f'{self.type} за' == f'{data[index -1]} {el}' or f'{self.type} за' == f'{data[index -2]} {data[index -1]} {el}':
                self.total = int(data[index + 1])
            elif '(' in el:
                self.cost = int(el.replace('(', ''))

    def __str__(self):
        text = f'Type:{self.type}'
        if self.buy:
            text = f'{text}, buy'
        if self.sell:
            text = f'{text}, sell'
        text = f'{text}, count:{self.count}, total:{self.total}, {self.cost} cost/unit'
        return text

    def __repr__(self):
        return self.__str__()
