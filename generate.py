# 本文件存放生成下一步可选行棋的函数

import numpy as np

import const
import evaluate


def generate(gobang_board, player=const.AI):
    # 本函数在选择节点时加入下子点评估，按照得分对可能位置进行排序，并且仅保留前LIMIT_GENERATE_NUM个
    # 评估时需要知道当前是谁下
    LIMIT = const.LIMIT_GENERATE_NUM
    moves = set()
    drct_list = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1),
                 (1, 0), (1, -1), (0, -1))  # 一个子的周围一圈位置

    for r in range(const.SIDE_LEN):
        for c in range(const.SIDE_LEN):
            if gobang_board[r][c] != const.EMPTY:
                for each_drct in drct_list:
                    dr, dc = each_drct
                    if 0 <= r+dr < const.SIDE_LEN and 0 <= c+dc < const.SIDE_LEN and gobang_board[r+dr][c+dc] == const.EMPTY:
                        # 若在范围内且为空，则插入moves集合
                        moves.add((r+dr, c+dc))

    moves = list(moves)
    score_and_num_list = []  # 二元组，第一个元素存得分，第二个元素存下标
    for i in range(len(moves)):
        r, c = moves[i]
        # __move(gobang_board, player, (r, c))
        # 得分中加入位置得分，便于ai尽量往中间走
        score = evaluate.evaluate_point(
            gobang_board, player, (r, c))+const.POS_SCORE[r][c]
        score_and_num_list.append((score, i))
        # __remove(gobang_board, (r, c))

    # 使用极大极小思想对生成位置排序
    if_reverse = True if player == const.MAX_P else False
    score_and_num_list.sort(reverse=if_reverse)   # 按照分数进行排序
    final_moves = []
    for i in range(min(LIMIT, len(score_and_num_list))):    # 保证生成不超过LIMIT个
        which = score_and_num_list[i][1]  # 取下标
        final_moves.append(moves[which])

    return final_moves


if __name__ == "__main__":
    # 测试用例
    H = const.HUMAN
    A = const.AI
    gobang_board = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, A, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, H, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, H, H, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, A, H, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, H, A, H, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, H, A, A, A, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ])

    moves = generate(gobang_board, const.AI)
    print(moves)
