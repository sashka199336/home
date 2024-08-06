class House:
    def __init__(self,name,number_of_floors):
        self.name=name
        self.number_of_floors=number_of_floors


    def go_to(self,new_floor):
        self.new_floor=new_floor
        if self.number_of_floors<self.new_floor or self.new_floor<1 :
         print('Такого этажа не существует')
        else:
            print(new_floor)


h1 = House('ЖК Бомж', 15)
h2 = House('Развалюха', 6)
print(h1.name,h1.number_of_floors)
print(h2.name,h2.number_of_floors)
h1.go_to(51)
h2.go_to(4)
