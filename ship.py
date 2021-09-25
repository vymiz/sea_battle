from dot import Dot
class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self): # возвращает все точки из которых состоит корабль
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i

            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots

if __name__ == '__main__':
    from dot import Dot
    s = Ship(Dot(1,2), 3, 0)
    print(s)
    print(s.dots)
    print(s.shooten(Dot(2,2)))