class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        args = args[0]
        cls.houses_history.append(args)
        return instance


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        if isinstance(number_of_floors, House):
            self.houses_history = number_of_floors.append()

    def __del__ (self):
        print(self.name, ' снесён, но он останется в истории')








h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
