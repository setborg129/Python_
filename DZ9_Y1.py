from time import sleep




class TrafficLight:
    x = 0

    def __init__(self):
        self.__colors = None

    def running(self):
        for x in range(0, 101):
            print(f"\rКрасный сфетофор {x}%", end=" ")
            sleep(0.07)

        for x in range(0, 101):
            print(f"\rЖелтый сфетофор {x}%", end=" ")
            sleep(0.02)

        for x in range(0, 101):
            print(f"\rЗеленый сфетофор {x}%", end=" ")
            sleep(0.01)

if __name__ == '__main__':
    light = TrafficLight()
    light.running()