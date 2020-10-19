import json
import math
import os

class Config:
    ENV_VAR_NAME = "HOMEPATH"

    def __init__(self, config_path):
        self.path = config_path
        # self.path = "config.json"
        self._data = {}
        self.read

    @classmethod
    def load_from_env(cls):
        config_path = os.environ[cls.ENV_VAR_NAME]
        print(config_path)
        return cls('config.json')

        # a =  os.environ
        # for k, v in a.items():
        #     print(k + " " + v)

        # a = cls('config.json')
        # print(a.read())
        # print(a)

    @property
    def read(self):
        # print(self.path)
        with open(self.path) as fd:
            self._data = json.load(fd)
            return self._data

    def __getitem__(self, item):
        return self._data[item]

    @property
    def db_connection_uri(self):
        section = self._data["database"]
        return 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(**section)

    # @staticmethod
    # def list_static(static_path):
    #     ret = []
    #     for path in os.listdir(static_path):
    #         _, ext = os.path.splitext(path)
    #         if ext in ['.js', "http", ".png"]:
    #             ret.append(path)
    #     return ret


cfg = Config.load_from_env()
# cfg.read
# print(cfg['server']['port'])


# cfg = Config.load_from_env()
# static_path = cfg['static_path']
# print(cfg.list_static(static_path))

# class Circle:
#     """
#     Тестирование property
#     """
#     def __init__(self):
#         self.radius = 0
#
#
#     @property
#     def area(self):
#         # print(str(self.radius) + ' - это радиус')
#         return 3.1415 * self.radius ** 2
#
#     @area.setter
#     def area(self, value):
#         self.radius = math.sqrt(value / 3.1415)
#
#         # print(self.radius, value)
#
# a = Circle()
# a.area = 10
# print(a.area)