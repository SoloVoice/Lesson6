class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False

    def go(self):
        print("Машина едет")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direct):
        print(f"Машина повернула в{direct}")

    def show_speed(self):
        print(f"Скорость автомобиля: {self.speed}")

    def __init__(self):
        print(f"Марка автомобиля: {self.name}")
        print(f"Цвет автомобиля: {self.color}")
        print(f"Полицейский автомобиль: {self.is_police}")
        print(f"Скорость автомобиля: {self.speed}")


class TownCar(Car):
    speed = 80
    color = "green"
    name = "Nissan"
    is_police = False

    def show_speed(self):
        if self.speed <= 60:
            print(f"Скорость автомобиля: {self.speed}")
        else:
            print(f"Вы превысили скорость! Максимально разрешенная скорость 60!")

    def __init__(self):
        super().__init__()
        self.show_speed()


class SportCar(Car):
    speed = 180
    color = "red"
    name = "Dodge"
    is_police = False


class WorkCar(Car):
    speed = 140
    color = "silver"
    name = "Ford"
    is_police = False

    def show_speed(self):
        if self.speed <= 40:
            print(f"Скорость автомобиля: {self.speed}")
        else:
            print(f"Вы превысили скорость! Максимально разрешенная скорость 40!")

    def __init__(self):
        super().__init__()
        self.show_speed()


class PoliceCar(Car):
    speed = 230
    color = "blue"
    name = "Mercedes"
    is_police = True


a = TownCar()
print("")
b = SportCar()
print("")
c = WorkCar()
print("")
d = PoliceCar()
