import random
import math


class RandomAgent:
    """Agent that picks a random available move.  You should be able to beat it."""
    def get_move(self, state, depth=None):
        possibles =  list( state.successors())
        return random.choice(possibles)


class HumanAgent:
    """Prompts user to supply a valid move."""
    def get_move(self, state, depth=None):
        move__state = dict(state.successors())
        prompt = "Kindly enter your move {}: ".format(sorted(move__state.keys()))
        move = int(input(prompt))
        return move, move__state[move]



class ComputerAgent:
    """Artificially intelligent agent that uses minimax to select the best move."""

    def get_move(self, state, depth=None):
        """Select the best available move, based on minimax value."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None

        for move, state in state.successors():
            util = self.minimax(state, depth)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, state
        return best_move, best_state

    def minimax(self, state, depth):
        """Determine the minimax utility value the given state.

        Args:
            state: a connect4.GameState object representing the current board
            depth: the maximum depth of the game tree that minimax should traverse before
                estimating the utility using the evaluation() function.  If depth is 0, no
                traversal is performed, and minimax returns the results of a call to evaluation().
                If depth is None, the entire game tree is traversed.

        Returns: the minimax utility value of the state
        """
        if depth == 0 or not state.winner() is None:
            return self.evaluation(state)
        elif depth is None:
            if state.next_player() == 1:
                value = - math.inf 
                for s in state.successors():
                    value = max(value,self.minimax(s[1],None))
                return value
            else:
                value = math.inf
                for s in state.successors():
                    value= min(value,self.minimax(s[1],None))
                return value
        else:
            if state.next_player() == 1:
                value =  -math.inf
                for s in state.successors():
                    value = max(value,self.minimax(s[1],depth-1))
                return value  
            else:
                value = math.inf
                for s in state.successors():
                    value = min(value,self.minimax(s[1],depth-1))
                return value 
        #
        # Fill this in!
        #  # Change this line!

    def evaluation(self, state):
        """Estimate the utility value of the game state based on features.

        N.B.: This method must run in O(1) time!

        Args:
            state: a connect4.GameState object representing the current board

        Returns: a heusristic estimate of the utility value of the state
        """
        #
        # Fill this in!
        #
        
        def Vertical(state, col,player):
            count = [0]
            board = state.board
            c = 0
            for i in range(state.num_rows):
                if board[i][col] == player:
                    c+= 1
                    count[-1] =c
                else:
                    count.append(c)
                    c = 0
            return max(count)
        
        def Horizontal(state,row,player):
            count = [0]
            board = state.board
            c = 0
            for j in range(state.num_cols):
                if board[row][j] == player:
                    c += 1
                    count[-1] = c
                else:
                    count.append(c)
                    c = 0
            return max(count)
        
        def Diagnal1(state,player):
            count1 = [0]
            board = state.board
            for i in range(6):
                c = 0
                row, col = i, 0
                while row < 6 and col < 7:  
                    if board[row][col] == player:
                        c += 1
                        count1[-1] = c
                    else:
                        count1.append(c)
                        c = 0
                    row+=1
                    col+=1
            for j in range(1,7):
                c = 0
                count1.append(0)
                row, col =0 ,j
                while row< 6 and col < 7:
                    if board[row][col] == player:
                        c += 1
                        count1[-1] = c
                    else:
                        count1.append(c)
                        c = 0
                    row += 1
                    col += 1
            return max(count1) ## implement this 
        
        
        
        def Diagnal2(state,player):
            count1 = [0]
            board = state.board
            for i in range(6):
                c = 0
                row, col = i, 0
                while row >= 0 and col < 7:  
                    if board[row][col] == player:
                        c += 1
                        count1[-1] = c
                    else:
                        count1.append(c)
                        c = 0
                    row+= -1
                    col+=1
            for j in range(1,7):
                c = 0
                count1.append(0)
                row, col =5 ,j
                while row >= 0 and col < 7:
                    if board[row][col] == player:
                        c += 1
                        count1[-1] = c
                    else:
                        count1.append(c)
                        c = 0
                    row += -1
                    col += 1
            return max(count1)
            
        
        
        player = state.next_player()
        
        if state.winner() == player:
            return 100000
        elif state.winner() == -player:
            return - 10000
        elif state.winner() == 0:
            return 0
        else:
            score = 0
            for i in range(state.num_rows):  
                    score += Horizontal(state, i,player) - Horizontal(state,i,-player)
            for j in range(state.num_cols): 
                    score += Vertical(state, j,player) - Vertical(state,j,-player)
            score += Diagnal1(state,player) - Diagnal1(state, -player) + Diagnal2(state, player)- Diagnal2(state, -player)
                        
            return score
                    
                    
                
         # Change this line!


class ComputerPruneAgent(ComputerAgent):
    """Smarter computer agent that uses minimax with alpha-beta pruning to select the best move."""

    def minimax(self, state, depth):
        util, pruned = self.minimax_prune(state, depth)
        return util

    def minimax_prune(self, state, depth , alpha = -math.inf, beta = math.inf):
        """Determine the minimax utility value the given state using alpha-beta pruning.

        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to to column 1.

        Args: see ComputerAgent.minimax() above

        Returns: the minimax utility value of the state, along with a list of state objects that
            were not expanded due to pruning.
        """
        #
        # Fill this in!
        #
        unexpanded =[]
        if depth == 0 or not state.winner() is None:
            return self.evaluation(state), unexpanded
        elif depth is None:
            if state.next_player() == 1:
                value = - math.inf
                for s in state.successors():
                    value =max(value,self.minimax_prune(s[1], None,alpha,beta)[0])
                    alpha = max(value,alpha)
                    if alpha >= beta:
                        unexpanded.append(s[1])
                        break
                return value, unexpanded 
            else:
                value = math.inf
                for s in state.successors():
                    value = min(value,self.minimax_prune(s[1], None,alpha,beta)[0])
                    beta = min(beta,value)
                    if alpha >= beta:
                        unexpanded.append(s[1])
                        break
                return value, unexpanded 
        else:
            if state.next_player() == 1:
                value = - math.inf
                for s in state.successors():
                    value = max(value,self.minimax_prune(s[1],depth-1,alpha,beta)[0])
                    alpha = max(value,alpha)
                    if alpha >= beta:
                        unexpanded.append(s[1])
                        break
                return value,unexpanded 
            else:
                value = math.inf
                for s in state.successors():
                    value = min(value,self.minimax_prune(s[1], depth -1,alpha,beta)[0])
                    beta = min(beta,value)
                    if alpha >= beta:
                        unexpanded.append(s[1])
                        break
                return value,unexpanded  # Change this line!


