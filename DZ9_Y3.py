class Worker:
    def __init__(self, name, surname, income, position):
        self.name     = name
        self.surname  = surname
        self._income   = income
        self.position = position

class Position(Worker):
    def get_full_name(self):
        return (f'{self.name} , {self.surname}')

    def get_total_income(self):
        return  self._income["wage"] + self._income["bonus"]


incomes = {'wage': 15, 'bonus': 50}
positions = Position('Max', 'Yulia', incomes, 'GrandMaster')
print(positions.get_total_income())
print(positions.get_full_name())