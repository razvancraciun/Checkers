# def heuristic(state):
#     result = 0
#     for i in range(BOARD_SIZE):
#         for j in range(BOARD_SIZE):
#             if state[0][i][j] == NPIECE:
#                 result += (BOARD_SIZE - i + 1) * state[0][i][j]
#             elif state[0][i][j] == -NPIECE:
#                 result += (i + 1) * state[0][i][j]
#             elif state[0][i][j] == SPIECE:
#                 result += (i + 1) * 2 * state[0][i][j]
#             elif state[0][i][j] == -SPIECE:
#                 result += (BOARD_SIZE - i + 1) * 2 * state[0][i][j]
#     return result