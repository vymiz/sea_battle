from dot import Dot
from exceptions import *

class Board:
    def __init__(self, hid = False, size = 6):
        self.size = size
        self.hid = hid # скрываем корабли на доске

        self.count = 0 # количество пораженных кораблей

        self.field = [ ["O"]*size for _ in range(size) ] # сетка игрового поля

        self.busy = [] # клетки,занятые либо кораблем, либо выстрелом
        self.ships = [] # список кораблей на доске

    def add_ship(self, ship): # добавление корабля на доску

        for d in ship.dots:
            if self.out(d) or d in self.busy: # проверка доступности клетки для размещения корабля
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb = False): # заполняем точками поля, куда нельзя ставить корабли, т.к. близко уже имеющийся корабль
        near = [
            (-1, -1), (-1, 0) , (-1, 1),
            (0, -1), (0, 0) , (0 , 1),
            (1, -1), (1, 0) , (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                # self.field[cur.x][cur.y] = '+'
                if not(self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def __str__(self): # отрисовываем доску
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i+1} | " + " | ".join(row) + " |"

        if self.hid: # скрываем корабли, если hid == True
            res = res.replace("■", "O")
        return res

    def out(self, d): # проверка нахождения точки в пределах доски
        return not((0<= d.x < self.size) and (0<= d.y < self.size))

    def shot(self, d): # стреляем по доске
        if self.out(d): # проверка координат выстрела - на доске ли?
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d) # добавляем координат выстрела в список использованных клеток

        for ship in self.ships: # если попали, уменьшаем жизнь корабля на 1 и ставим Х в место попадания
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0: # если потопили
                    self.count += 1
                    self.contour(ship, verb = True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d.x][d.y] = "."
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []

if __name__ == '__main__':
    from dot import Dot
    from ship import Ship
    from exceptions import *
    b = Board()
    # print(b)
    s = Ship(Dot(1,2), 3, 0)
    # print(s.dots)
    b.add_ship(s)
    print(b)