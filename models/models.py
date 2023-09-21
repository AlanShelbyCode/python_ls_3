from framework.models import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, id, location, name, director_id):
        try:
            # ніби якщо такий вже є воно його переписує не змінуючи значень
            plant = self.get_by_id(id)
            #print(self.get_by_id(id))
            self.id = id
            self.location = plant['location']
            self.name = plant['name']
            self.director_id = plant['director_id']
        except Exception:
            self.id = id
            self.location = location
            self.name = name
            self.director_id = director_id
            if self.director() is None:
                del self
                raise Exception("We don't have employee with this id!")

    def director(self):
        try:
            director = Employee.get_by_id(self.director_id)
            return director
        except Exception:
            return None

    @classmethod
    def get_plant_by_director_id(cls, director_id):
        plants = cls.get_file_data(cls.file)
        #масив plants
        for plant in plants:
            if plant['director_id'] == director_id:
                return plant
        return None
    # def _generate_dict(self):
    #     return {
    #         'id': self.id,
    #         'location': self.location,
    #         'name': self.name,
    #         'director_id': self.director_id
    #     }

    # def save(self):
    #     plant_in_dict_format = self._generate_dict()
    #     plants = self.get_file_data(self.file)
    #     plants.append(plant_in_dict_format)
    #     try:
    #         element = self.get_by_id(self.id)
    #     except Exception:
    #         self.save_to_file(plants)
class Employee(Model):
    file = "employees.json"

    def __init__(self, id, name, email, department_type, department_id, salon_id):
        self.id = id
        self.name = name
        self.email = email
        self.department_type = department_type
        self.department_id = department_id
        self.salon_id = salon_id
        self.is_director = False
        self.is_salon_director = False

        if Plant.get_plant_by_director_id(self.id) is not None:
            self.is_director = True
        if Salon.get_salon_by_salon_director_id(self.id) is not None:
            self.is_salon_director = True

    def department(self):
        if self.department_type == "plant":
            return Plant.get_by_id(self.deparment_id)
        return None

class Salon(Model):
    file = "salons.json"

    def __init__(self, id, location, name, salon_director_id):
        try:
            salon = self.get_by_id(id)
            self.id = id
            self.location = salon['location']
            self.name = salon['name']
            self.salon_director_id = salon['salon_director_id']
        except Exception:
            self.id = id
            self.location = location
            self.name = name
            self.salon_director_id = salon_director_id
            if self.salon_director_id(self.id) is None:
                del self
                raise Exception("We don't have employee of salon with this id!")

    def salon_director(self):
        try:
            # у випадку true
            salon_director = Employee.get_by_id(self.salon_director_id)
            return salon_director
        except Exception:
            return None

    def get_salon_by_salon_director_id(cls, salon_director_id):
        salons = cls.get_file_data(cls.file)
        #масив salons
        for salon in salons:
            if salon['salon_director_id'] == salon_director_id:
                return salon
        return None