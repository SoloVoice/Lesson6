class Road:
    _length = 0
    _width = 0

    def __init__(self):
        self._length = int(input("Введите длинну полотна: "))
        self._width = int(input("Введите ширину полотна: "))
        print(f"Необходимая масса асфальта: {self._length*self._width*25*5}")


a = Road()
