import ticTacToe

field = ticTacToe.Field(3, 3)

p1 = ticTacToe.Player("Ivan", 0, field)
p2 = ticTacToe.Player("Dima", 1, field)

game = ticTacToe.Game(field, p1, p2)
game.start()