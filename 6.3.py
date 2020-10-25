class Worker:
    name = "Иван"
    surname = "Иванов"
    position = "Грузчик"
    _income = {"salary": 280, "bonus": 500}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.surname} {self.name}")

    def get_total_income(self, hours):
        print((Worker._income.get("salary")*hours) + Worker._income.get("bonus"))


a = Position()
a.get_full_name()
total_hours = int(input("Сколько часов отработал сотрудик: "))
a.get_total_income(total_hours)
