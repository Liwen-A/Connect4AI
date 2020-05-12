
"""Test boards for Connect4

Place test boards in this module to help test your code.  Note that ince connect4.GameState
stores board contents as a 0-based list of lists, these boards are reversed to they can be written
right side up here.
"""

from agents import ComputerAgent

board1 = reversed([ [  0,  0,  0,  0,  0,  0,  0 ],  # You should modify these!
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  1, -1,  0,  0,  0,  0,  0 ],
                    [  1, -1,  0,  0,  0,  0,  0 ],
                    [  1, -1,  0,  0,  0,  0,  0 ] ])

board2 = reversed([ [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0, -1, -1, -1,  0,  0 ],
                    [  0,  0,  1,  1,  1,  0,  0 ] ])

board3 = reversed([ [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  1, -1,  1,  1,  0 ] ])


class test:
    
    def __init__(self, boards,nrows=6, ncols=7):
        self.num_rows = nrows
        self.num_cols = ncols 
        self.board = boards
        
    def next_player(self):
        return 1
    
    
    def winner(self):
        return None



test1 = test(list(board1))
test2 = test(list(board2))
test3 = test(list(board3))
agent= ComputerAgent()
print(agent.evaluation(test3))