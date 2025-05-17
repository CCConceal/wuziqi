import const
def print_board(board):
    symbol = {const.EMPTY: '.', const.HUMAN: '●', const.AI: '○'}
    for row in board:
        print(' '.join(symbol[v] for v in row))
    print()
