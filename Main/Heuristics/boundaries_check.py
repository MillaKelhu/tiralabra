# from Ohjelma.alphabeta import TicTacToe


def boundaries_check(tictactoe, mark: str):
    distance = 0
    table = []
    for i in range(tictactoe.board_size):
        rivi = tictactoe.state[
            i * tictactoe.board_size : (i + 1) * tictactoe.board_size
        ]
        table.append(rivi)
    # for r in table:
    #     print(r)

    for i in range(tictactoe.board_size):
        for j in range(tictactoe.board_size):
            if table[j][i] == mark:
                distance += min(j, tictactoe.board_size - j) + min(
                    i, tictactoe.board_size - i
                )
    # print("distance", distance)
    maximum = (tictactoe.board_size / 2) * tictactoe.board_size ** 2
    relation = distance / maximum
    # print("relation", relation)
    return relation
