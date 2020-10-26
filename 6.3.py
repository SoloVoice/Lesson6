class Worker:
    name = "Иван"
    surname = "Иванов"
    position = "Грузчик"
    _income = {"salary": 280, "bonus": 500}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.surname} {self.name}")

    def get_total_income(self):
        hours = int(input("Сколько часов отработал сотрудик: "))
        print((Worker._income.get("salary")*hours) + Worker._income.get("bonus"))

    def __init__(self):
        self.get_full_name()
        self.get_total_income()


a = Position()
