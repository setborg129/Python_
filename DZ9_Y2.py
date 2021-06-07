class Road:
    _length = 5000  # длина в метрах
    _width = 20  # Ширина в метрах
    weight = 25  # масса на 1 кв м. асфальта
    thickness = 5  # толщина см

    def calculation(self):
        result = self._length * self._width * self.weight * self.thickness
        result = int(result / 1000)
        print(f'Результ = {result} т.')

cls = Road()

cls.calculation()
