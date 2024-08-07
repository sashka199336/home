class House:
    def __init__(self,name,number_of_floors):
        self.name=name
        self.number_of_floors=number_of_floors


    def go_to(self,new_floor):
        if (new_floor <= self.number_of_floors) and (new_floor >= 1):
                for i in range(1, new_floor + 1):
                    print(i)
        else:
                print('"Такого этажа не существует"')


h1 = House('ЖК Бомж', 15)
h2 = House('Развалюха', 6)
print(h1.name,h1.number_of_floors)
print(h2.name,h2.number_of_floors)
h1.go_to(15)
h2.go_to(7)
