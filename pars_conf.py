import json
import math

class Config:
    def __init__(self, config_path):
        self.path = config_path
        self._data = {}
    @property
    def read(self):
        with open(self.path, 'r') as fd:
            self._data = json.load(fd)
            # print(json.load(fd))

    def __getitem__(self, item):
        return self._data[item]

cfg = Config('config.json')
cfg.read
print(cfg['server']['host'])

class Circle:
    def __init__(self):
        self.radius = 0


    @property
    def area(self):
        print(str(self.radius) + ' - это радиус')
        return 3.1415 * self.radius ** 2

    @area.setter
    def area(self, value):
        self.radius = math.sqrt(value / 3.1415)
        # self.radius = value

        print(self.radius, value)

a = Circle()
a.area = 3
print(a.area)