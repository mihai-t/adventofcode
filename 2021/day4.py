import os


def check_win(board, el_i, el_j):
    line, col = True, True
    available = set(board.values())
    for q in range(0, 5):
        if (el_i, q) in available:
            col = False
            break
    for q in range(0, 5):
        if (q, el_j) in available:
            line = False
            break
    return line or col


def say_number(n, board, wins):
    w_board_index = []
    for board_index in range(len(board)):
        if board_index in wins:
            continue
        if n in board[board_index]:
            v = board[board_index][n]
            del board[board_index][n]
            if check_win(board[board_index], v[0], v[1]):
                w_board_index.append(board_index)
    return w_board_index


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day4.txt'), 'r') as f:
        lines = f.readlines()
        numbers = list(map(int, lines[0].split(',')))
    board_index = 0
    i = 0
    board = {}
    for line in lines[2:]:
        if line == '\n':
            board_index += 1
            i = 0
            continue
        nr = list(map(lambda x: int(x), filter(lambda x: x, line.split(' '))))
        assert len(nr) == 5
        if i == 0:
            board[board_index] = {}
        for j in range(0, len(nr)):
            assert nr[j] not in board[board_index]
            board[board_index][nr[j]] = (i, j)
        i += 1
    print(len(board), 'boards')
    wins = set()
    for n in numbers:
        w_board_indexes = say_number(n, board, wins)
        if w_board_indexes:
            for w_board_index in w_board_indexes:
                s = sum(board[w_board_index].keys())
                print('board', w_board_index, n, '*', s, '=', n * s)
                wins.add(w_board_index)
    assert len(wins) == len(board)
