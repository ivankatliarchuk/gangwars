# -*- coding: utf-8 -*-

resources = ['Трава', 'Бокситы', 'Уран', 'Маковая соломка', 'Сталь', 'Алюминий']
resexp = {
    'Уран' : {
        10:1
    },
    'Сталь' : {
        5:1
    },
    'Бокситы': {
        10:2
    },
    'Маковая соломка': {
        10:1
    },
    'Алюминий': {
        5:1
    }
}

class Resource:

    def __init__(self, object_id, data):
        self.object_id = object_id
        self.data = data
        self.txt = ' '.join(data)
        self.buy = False
        self.sell = False

        for res in resources:
            if res in ' '.join(data):
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
                self.total = data[index + 1]
            elif '(' in el:
                self.cost = el.replace('(', '')



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
