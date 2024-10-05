from threading import Thread
from time import sleep

class Knight(Thread):
    count_of_enemy = 100
    count_of_days = 0

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.count_of_enemy > 0:
            self.count_of_enemy = self.count_of_enemy - self.power
            self.count_of_days += 1
            sleep(1)
            print(f'{self.name} сражается {self.count_of_days} дней, осталось {self.count_of_enemy} воинов.\n')
        print(f'{self.name} одержал победу спустя {self.count_of_days} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
