import ticTacToe_lib
import time


field = ticTacToe_lib.Field(2, 2)
time.sleep(1)

field.getInfo()
time.sleep(1)
field.draw()
time.sleep(1)
field.getCells()