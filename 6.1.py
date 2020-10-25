from time import sleep


class TrafficLight:
    __colour = ["красный", "желтый", "зеленый", "желтый"]

    def running(self):
        while True:
            for i in TrafficLight.__colour:
                if i == "красный":
                    print(f"Цвет светофора: {i}")
                    sleep(7)
                elif i == "желтый":
                    print(f"Цвет светофора: {i}")
                    sleep(2)
                elif i == "зеленый":
                    print(f"Цвет светофора: {i}")
                    sleep(5)


a = TrafficLight()
a.running()
