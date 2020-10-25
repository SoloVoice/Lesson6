class Road:
    _length = 0
    _width = 0

    def calculation(self):
        print(f"Необходимая масса асфальта: {self._length*self._width*25*5}")


a = Road()
a._length = int(input("Введите длинну полотна: "))
a._width = int(input("Введите ширину полотна"))
a.calculation()
