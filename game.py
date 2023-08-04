class Game:

    def __init__(self, players: tuple[str]) -> None:
        self.players = players
        self.player_turn = 0
        self.board: list[int] = [None] * 9

    def __str__(self) -> str:
        board = f"""
players: {self.players[0]} - {self.players[1]}
{self.players[self.player_turn]}'s turn
board: {self.get_board_line(0)}
       ---------
       {self.get_board_line(1)}
       ---------
       {self.get_board_line(2)}
"""
        winner = self.check_winner()
        winner_line = f'winner: {self.players[winner]}' if winner is not None else ''
        return board + winner_line

    def get_row_values(self, row: int) -> list[int]:
        return self.get_cell_values(range(row * 3, (row + 1) * 3))

    def get_column_values(self, column: int) -> list[int]:
        return self.get_cell_values(x * 3 + column for x in range(3))
    
    def get_diagonal_values(self, diag: int) -> tuple[int]:
        return self.get_cell_values(x * 4 + (2 * diag * (1 - x)) for x in range(3))

    def get_board_line(self, line: int) -> str:
        return ' | '.join(self.get_cell_mark(cell) for cell in self.get_row_values(line))

    def get_cell_mark(self, value: int) -> str:
        mapping = {0: 'O', 1: 'X'}
        return mapping.get(value, ' ')

    def get_cell_values(self, cells: tuple[int]) -> list[int]:
        return [self.board[cell] for cell in cells]

    def add_move(self, cell: int) -> int:
        if self.board[cell] is not None: raise Exception('Invalid move')
        self.board[cell] = self.player_turn
        self.player_turn = 1 - self.player_turn
        return self.check_winner()

    def check_winner(self) -> int:
        # checking rows first
        for row in range(3):
            row_values = self.get_row_values(row)
            winner = self.check_complete_line(row_values)
            if winner is not None: break

        # checking columns
        if winner is None:
            for column in range(3):
                column_values = self.get_column_values(column)
                winner = self.check_complete_line(column_values)
                if winner is not None: break

        # checking diagonals
        if winner is None:
            for diag in range(2):
                diagonal_values = self.get_diagonal_values(diag)
                winner = self.check_complete_line(diagonal_values)
                if winner is not None: break

        if winner is None and not None in self.board:
            winner = -1
        return winner

    def check_complete_line(self, values: tuple[int]) -> int:
        first = values[0]
        if first is not None and len(set(values)) == 1:
            return first
        else: 
            return None