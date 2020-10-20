import json
import math
import os

class Config:
    ENV_VAR_NAME = "NEW_VAR"

    def __init__(self, config_path):
        self.path = config_path
        self._data = {}
        self.read

    @classmethod
    def load_from_env(cls):
        """
        Обращаемся к переменным среды и отправляем полученный путь
        в класс Config
        :return:
        """
        config_path = os.environ[cls.ENV_VAR_NAME]
        return cls(config_path)

    @property
    def read(self):
        """
        Функция выводит прочитаный json файл в виде словаря _data
        :return:
        """
        with open(self.path) as fd:
            self._data = json.load(fd)
            return self._data

    def __getitem__(self, item):
        return self._data[item]

    @property
    def db_connection_uri(self):
        """
        Генерирует и выводит строку из конфиг файла
        """
        section = self._data["database"]
        return 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(**section)

    @staticmethod
    def list_static(static_path):
        """
        отображает файлы с указаным именем
        :param static_path:
        :return:
        """
        ret = []
        for path in os.listdir(static_path):
            # print(path)
            _, ext = os.path.splitext(path)
            if ext in ['.js', "http", ".json"]:
                ret.append(path)
        return ret

cfg = Config.load_from_env()
static_path = cfg['static_dir']

print(cfg.list_static(static_path))
print(cfg["server"])
print(cfg.db_connection_uri)

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