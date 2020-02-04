from time import sleep

class Light:
    __color = ['Красный', 'Желтый', 'Зеленый', 'Желтый']

    def run(self):
        i = 0
        while i < 4:
            print(f'Светофор переключается \n '
                  f' {Light.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(3)
            elif i == 2:
                sleep(7)
            elif i == 3:
                sleep(3)
            i += 1


Light = Light()
Light.run()