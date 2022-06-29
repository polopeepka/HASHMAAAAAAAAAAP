import random

class Spin:

    def __init__(self, spin, stop, win, lose):
        self.spin = spin,
        self.stop = stop,
        self.win = win,
        self.stop = stop

    def win_spinner (self):
        while True:
            duw = input('Выбирите чисо от 1 до 100 - ')
            if duw == (1, 100):
                rand = random.randint(1, 100)
            else:
                print('ТОлько от 1 до 100')
                break
            if duw == rand:
                print(f'Spinner {self.spin} was stopped and u {self.win}')
            else:
                print('что то не так!')
                continue

    def lose_spinner(self):
        while True:
            duw = input('Выбирите чисо от 1 до 100 - ')
            if duw == (1,100):
                rand = random.randint(1, 100)
            else:
                print('ТОлько от 1 до 100')
                break
            rand = random.randint(1, 100)

            if duw != rand:
                print(f'Spinner {self.spin} was stopped and after u {self.win}')
            else:
                print('что то не так!')
                continue
        print(f'Spinner {self.stop} was stopped')

    def start(self):

        while True:
            ask = input('Хотите начать игру? - ')
            if ask == 'да':
                print(f'Spinner {self.spin} was started')
            elif ask == 'нет':
                print('Пока,удачки')
            else:
                break

    def stop(self):
        while True:
            ask = input('Хотите закончить игру? - ')
            if ask == 'да':
                print(f'Spinner {self.spin} was stopped')
            elif ask == 'нет':
                print('Спасибо за игру')
            else:
                break









