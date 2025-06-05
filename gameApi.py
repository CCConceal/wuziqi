
from typing import Tuple, List
import const

import numpy as np
import const
import evaluate
import AI_action
from AI_action import gobang_board

def play_turn(human_move):
    global gobang_board
    r, c = human_move
    r = r-1
    c = c-1

    if gobang_board[r][c] != const.EMPTY:
        raise ValueError("该位置已经有棋子！")

    # 人类落子
    gobang_board[r][c] = const.HUMAN

    # 判断人类是否获胜
    if evaluate.judge_game_win(gobang_board, (r, c)):
        return r, c, 1  # 人类胜，返回落子位置和状态1

    # AI落子
    ai_r, ai_c = AI_action.alpha_beta(gobang_board, const.AI, const.DEPTH)
    gobang_board[ai_r][ai_c] = const.AI

    # 判断AI是否获胜
    if evaluate.judge_game_win(gobang_board, (ai_r, ai_c)):
        return ai_r+1, ai_c+1, 2  # AI胜，状态2

    return ai_r+1, ai_c+1, 0  # 未分胜负，状态0

