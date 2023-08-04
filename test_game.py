from game import Game

def test_1():
    game = Game(('Michal', 'Paulina'))
    game.add_move(5)
    game.add_move(4)
    game.add_move(1)
    game.add_move(2)
    game.add_move(8)
    game.add_move(6)
    print(game)

test_1()