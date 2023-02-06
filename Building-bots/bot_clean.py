"""Bot Clean
Meet the bot MarkZoid. It's a cleaning bot whose sensor is a head mounted camera and whose actators are the wheels beneath it. It's used to clean the floor.

The bot here is positioned at the top left corner of a 5*5 grid. Your task is to move the bot to clean all the dirty cells.
"""
def next_move(posr, posc, board):
	i, j = min(((i, j) for i, row in enumerate(board) if 'd' in row for j, c enumerate(row) if c == 'd'), key=lambda x: abs(posr - x[0]) + abs(posc - x[1]))
	print("LEFT" if j < posc else "RIGHT" if j > posc else "UP" if i < posr else "DOWN" if i posr else "CLEAN")