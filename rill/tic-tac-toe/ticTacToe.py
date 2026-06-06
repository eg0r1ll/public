import config



class Cell:
    def __init__(self, x, y, status = None):
        self.id = id
        self.x_prob = x
        self.y_prob = y
        self.y = y // 2  
        self.x = int((x + 3) / 4 - 1)
        self.status = status

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.status}"


    def getInfo(self):
        print(f"cell: coord=({self.x_prob}, {self.y_prob}), coord_prob=({self.x}, {self.y}); status: {self.status}")


    def draw(self):
        if self.status == None:
            print(' ', end='')
        elif self.status:
            print(config.cross, end='')
        else:
            print(config.nought, end='')


    def getCoord(self):
        return (self.x, self.y)


    def getProbCoord(self):
        return (self.x_prob, self.y_prob)


    def chekCoord(self, coord):
        if coord == self.getCoord():
            return True
        else: 
            return False


    def changeFlag(self, player):
        if player == 0:
            self.status = False
        else: 
            self.status = True



class Field:
    def __init__(self, x = 3, y = 3, win = 3, start_draw = (0, 0)):
        self.x = x
        self.y = y
        self.win = win
        self.start_draw = start_draw

        # посимвольное представление x и y:
        self.x_probels = x * 4 - 1 # x = 4n - 1
        self.y_probels = y * 2 - 1 # y = 2n - 1

        #
        self.temp_x_coord = []

        # создание списка клеток (объектов)
        self.cells = dict()
        self._createCells()

     # создаем клетки
    def _createCells(self):     
        for x in range(self.x_probels):
            if ((x + 3) / 4) % 1 == 0: # x=4n-3 (1, 5, 9); 4n=x+3; n=(x+3)/4 | определение id символа где должен рампологаться крестик/нолик
                self.temp_x_coord.append(x)
        
        # !!! проверка на четность y не самое лучшее решение
        for y in range(self.y_probels):
            if y % 2 == 0:
                for x in self.temp_x_coord:
                    self.cells[(x, y)] = Cell(x, y) # !!! возможно не стоит в словарь пихать, а ограничиться списком т.к. x и y хранятся в самом объекте


    def getInfo(self):
        print(f"{self.x}x{self.y} ({self.x_probels}x{self.y_probels}); win={self.win}; start_draw_point={self.start_draw}")


    def _getCells(self):        
        return self.cells


    def checkWin(self):
        pass

    # отрисовка линии разделителя
    def _drawSeparation(self): 
        temp_string = ""
        for i in range(self.x_probels):
            if (i + 1) % 4 == 0:
                temp_string += config.crosshair
            else:
                temp_string += config.line
        print(temp_string)

    # отрисовка линии игрового поля
    def _drawLine(self, y): 
        for x in range(self.x_probels):
            if x in self.temp_x_coord: # отрисовка клетки
                self.cells[(x, y)].draw()
            elif ((x + 1) / 4) % 1 == 0: # x=4n-1 (3, 7, 11, 15 ...); 4n=x+1; n=(x+1)/4 | определение id символа где должна располагаться перегородка
                print(config.partition, end = "")
            else: # отрисовка пробелов
                print(" ", end = "")


    def draw(self): # отрисовка поля
        for y in range(self.y_probels): 
            if y % 2 == 1:
                self._drawSeparation()
                continue
            self._drawLine(y)
            print()
             


class Player:
    def __init__(self, name, side, field):
        self.name = name
        self.side = side
        self.field = field
        self.cells = Field._getCells(field)

    def move(self):
        coord = tuple(map(int, input("coord:").split()))
        for cell in self.cells.values():
            if coord == cell.getCoord():
                cell.changeFlag(self.side)
                break



class Game:
    def __init__(self, field, player1, player2):
        self.field = field
        self.p1 = player1
        self.p2 = player2

    def start(self):
        while True:
            self.field.draw()
            self.p1.move()
            self.field.draw()
            self.p2.move()            