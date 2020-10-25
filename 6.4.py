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


class TownCar(Car):
    speed = 60
    color = "green"
    name = "Nissan"
    is_police = False

    def show_speed(self):
        if self.speed <= 60:
            print(f"Скорость автомобиля: {self.speed}")
        else:
            print(f"Вы превысили скорость! Ваша текущая скорость: {self.speed}")


class SportCar(Car):
    speed = 180
    color = "red"
    name = "Dodge"
    is_police = False


class WorkCar(Car):
    speed = 40
    color = "silver"
    name = "Ford"
    is_police = False

    def show_speed(self):
        if self.speed <= 40:
            print(f"Скорость автомобиля: {self.speed}")
        else:
            print(f"Вы превысили скорость! Ваша текущая скорость: {self.speed}")


class PoliceCar(Car):
    speed = 230
    color = "blue"
    name = "Mercedes"
    is_police = True

a = TownCar()
print(a.name)
print(a.color)
print(a.is_police)
a.go()
a.turn("лево")
a.speed = 100
a.show_speed()
a.stop()
print("")
b = PoliceCar()
print(b.name)
print(b.color)
print(b.is_police)
b.go()
b.turn("право")
b.speed = 200
b.show_speed()
b.stop()
