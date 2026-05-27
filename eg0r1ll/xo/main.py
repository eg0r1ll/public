class Cell:
    def __init__(self, id, x, y, status = False):
        self.id = id
        self.sym_coord = id * 4 + 2
        self.x = x
        self.y = y
        self.status = status

    def getCoord(self):
        return (self.x ,)

    def getInfo(self):
        print(self.id, self.sym_coord, self.status)





class Field:
    def __init__(self, x = 3, y = 3, win = 3, start_draw = (0, 0)):
        self.x = x
        self.y = y
        self.win = win
        self.start_draw = start_draw
        
        # символьное 
        self.cells = [Cell(id, self.x, self.y) for id in range(self.x * self.y)]

        # посимвольное представление x и y:
        self.x_probels = x * 4 - 1 # x = 4n - 1
        self.y_probels = y * 2 - 1 # y = 2n - 1

    

    def getCells(self):
        for i in self.cells:
            i.getInfo()



    def getInfo(self):
        print(f"{self.x}x{self.y} ({self.x_probels}x{self.y_probels}); win={self.win}; start_draw_point={self.start_draw}")



    def _drawSeparation(self):
        temp_string = ""
        for i in range(self.x_probels):
            if (i + 1) % 4 == 0:
                temp_string += "+"
            else:
                temp_string += "-"
        print(temp_string)

    def _drawLine(self):
        for x in range(self.x_probels):

            if ((x + 3) / 4) % 1 == 0: # x=4n-3 (1, 5, 9); 4n=x+3; n=(x+3)/4 | определение id символа где должен рампологаться крестик/нолик
                print("#", end = "") 

            elif ((x + 1) / 4) % 1 == 0: # x=4n-1 (3, 7, 11, 15 ...); 4n=x+1; n=(x+1)/4 | определение id символа где должна располагаться перегородка
                print("|", end = "")

            else:
                print(" ", end = "")

    def draw(self):
        for y in range(self.y_probels): 
            if y % 2 == 1:
                self._drawSeparation()
                continue

            self._drawLine()
            print()
             




class Player:
    pass



class Game:
    pass





field = Field(10, 10)
field.getInfo()
field.draw()



# сделать координты (символьные) для каждой клетки
# id: (x, y)
# 0: (1, 0), 1: (5, 0)