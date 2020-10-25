class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title} пишет чернилами")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} пишет грифилем")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title} пишет чем-то на спиртовой основе")


a = Pen()
a.title = "ручка"
a.draw()
b = Pencil()
b.title = "карандаш"
b.draw()
c = Handle()
c.title = "маркер"
c.draw()
