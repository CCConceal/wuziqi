
from typing import Tuple, List
import const
from main import move, get_move_ai, gobang_board
from board_utils import print_board

def play_turn(human_pos: Tuple[int, int]) -> Tuple[Tuple[int, int], List[List[int]]]:
    """
    human_pos : (row, col)  —— 图像识别给的人类落子坐标
    return    : (ai_pos, board_copy)
    """
    # 玩家落子
    move(const.HUMAN, human_pos)

    # AI对弈
    ai_pos = get_move_ai()
    move(const.AI, ai_pos)

    # 控制台显示
    print_board(gobang_board)

    #
    board_copy = [row[:] for row in gobang_board]
    return ai_pos, board_copy
