class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Координаты выходят за границу игрового поля!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Эта клетка уже использована"

class BoardWrongShipException(BoardException):
    pass