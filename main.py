import numpy as np

class gameboard():
    def __init__(self):
        self.board = np.full((6,7), -1) #Board representation
        self.turn = 0 #Player 0 or Player 1
    
    def move(self, pos:int):

        if self.board[0][pos] > -1:
            return False

        for i in reversed(range(self.board.shape[0])):
            if self.board[i][pos] == -1:
                self.board[i][pos] = self.turn
                break
        self.flip()
        return True
    
    def flip(self):
        if self.turn==0:
            self.turn=1
        else:
            self.turn=0

    def checkWin(self, player):
        
        #HORIZONTAL CHECKING

        for i in range(self.board.shape[0]):
            p_count = 0
            for j in range(self.board.shape[1]):

                if self.board[i][j] == player:
                    p_count+=1
                else:
                    p_count=0

                if p_count == 4:
                    return True
        
        #VERTICAL CHECKING

        for j in range(self.board.shape[1]):
            p_count = 0
            for i in range(self.board.shape[0]):

                if self.board[i][j] == player:
                    p_count+=1
                else:
                    p_count=0
                
                if p_count == 4:
                    return True

        ##DIAGONAL CHECKING##
        
        for t in range(2):
            b = self.board
            if(t==1):
                b = np.fliplr(self.board)
            for j in range(b.shape[1]-4):
                for i in range(self.board.shape[0]-3):
                    if b[i][j]==player and b[i+1][j+1]==player and b[i+2][j+2]==player and b[i+3][j+3]==player:
                        return True

        #if self.board[0][0]==player and self.board[1][1]==player and self.board[2][2]==player and self.board[3][3]==player:
            #return True

        return False

b = gameboard()

b.move(0)
b.move(1)
b.move(1)
b.move(2)
b.move(2)
b.move(3)
b.move(2)
b.move(3)
b.move(3)
b.move(4)
b.move(3)

print(b.checkWin(1))
print(b.board)


