class TreeNode:
    def __init__(self, board_status, turn):
        self._board_status = board_status
        self._turn = turn
        self._score = None
        self._children = []

    def grow(self):
        if self._evaluate(self._board_status) is not None:
            return

        for i in range(len(self._board_status)):
            for j in range(len(self._board_status[i])):
                if self._board_status[i][j] is None:
                    new_child = TreeNode(
                        [[self._turn if (r, c) == (i, j) else cell for c, cell in enumerate(row)] for r, row in enumerate(self._board_status)],
                        'O' if self._turn == 'X' else 'X'
                    )
                    new_child.grow()
                    self._children.append(new_child)

    def _evaluate(self, cur_board_status):
        for i in range(3):
            if all(cell == 'X' for cell in cur_board_status[i]):
                return 1  # "X" wins
            elif all(cell == 'O' for cell in cur_board_status[i]):
                return -1  # "O" wins
            if all(row[i] == 'X' for row in cur_board_status):
                return 1  # "X" wins
            elif all(row[i] == 'O' for row in cur_board_status):
                return -1 

        if all(cur_board_status[i][i] == 'X' for i in range(3)) or all(cur_board_status[i][2 - i] == 'X' for i in range(3)):
            return 1  # "X" wins diagonally
        if all(cur_board_status[i][i] == 'O' for i in range(3)) or all(cur_board_status[i][2 - i] == 'O' for i in range(3)):
            return -1  # "O" wins diagonally
    
        if not any(cell is None for row in cur_board_status for cell in row):
            return 0  # Draw

        return None

    def propagate_score(self):
        if all(not child for child in self._children):
            self._score = self._evaluate(self._board_status)
            return self._score

        # Recursively propagate scores for child nodes
        for child in self._children:
            child.propagate_score()

        # If the current node is a maximizing player's node
        if self._turn == 'X':
            max_score = max(child._score for child in self._children)
            self._score = max_score
            return max_score

        # If the current node is a minimizing player's node
        else:  # self._turn == 'O'
            min_score = min(child._score for child in self._children)
            self._score = min_score
            return min_score



def main():
    board = [
        ["O", "O", "X"],
        [None, None, "X"],
        ["O", "X", None]
    ]
    gameTreeRoot = TreeNode(board, "X")
    gameTreeRoot.grow()
    gameTreeRoot.propagate_score()
    print("Player X can win: ", gameTreeRoot._score == 1) 
    print(gameTreeRoot._score) # should be true


if __name__ == '__main__':
    main()