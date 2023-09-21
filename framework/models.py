from abc import ABC, abstractmethod
import json


class Model(ABC):
    file = 'default.json'

    def save(self):

        # створюю елемент в дікт форматі
        #print(self.__dict__)
        element_in_dict_format = self.__dict__
        #отримуємо масив дітків по назві файлу
        elements = self.get_file_data(self.file)
        # додаємо наш дікт в масив
        elements.append(element_in_dict_format)
        # якщо такий вже є то повертаємо той самий елемент
        try:
            element = self.get_by_id(self.id)
        # сейвимо якщо не повторюється
        except Exception:
            # записує в файл новий масив діктів
            self.save_to_file(elements)

    # def _generate_dict(self,menu_flag):
    #     print(self.__dict__)
    #     return self.__dict__
    #     # if menu_flag == 1:
        #     return {
        #                 'id': self.id,
        #                 'location': self.location,
        #                 'name': self.name,
        #                 'director_id': self.director_id
        #             }
        # elif menu_flag == 2:
        #     return {
        #                 'id': self.id,
        #                 'email': self.email,
        #                 'name': self.name,
        #                 'department_type': self.department_type,
        #                 'department_id': self.department_id
        #             }
        # else:
        #     Exception("Сan`t make a dict")

    @classmethod
    def get_by_id(cls, id):
        # повертає масив діктів вже записаних
        data = cls.get_file_data(cls.file)
       # print(data)
        # віддає дікт по нашому id
        for el in data:
            if el['id'] == id:
                return el
        raise Exception("Not found")

    @classmethod
    def get_all(cls):
        data = cls.get_file_data(cls.file)
        return data

    @staticmethod
    def get_file_data(file_name):
        file = open("database/" + file_name, 'r')
        #масив діктів json
        data = json.loads(file.read())
        #print(data)
        file.close()
        return data

    def save_to_file(self, data):
        #cтрінгуємо наш масив діктів
        data = json.dumps(data)
        #відкриваємо файл
        file = open('database/' + self.file, "w")
        # переписуємо значення
        file.write(data)
        file.close()
