"""This sets up a TicTacToe class. The basic structure is a two
dimensional representation of the 3x3 board.  Each location is
occupied by a token which is one of: " ", "X", "O".

In our very simple initial version, the user always goes first as X
and the program plays the opponent as O.  The opponent just makes a
random move."""

import random 

HUMAN   = 0
MACHINE = 1

YOU_WON = "Congratulations! You won!\n"
WELCOME = "\nWelcome to our Tic-Tac-Toe game!\nPlease begin playing."
YOU_TIED = "Looks like a tie. Better luck next time!\n"
YOU_LOST = "Sorry!  You lost!\n"

def initialBoard():
    return[ [" ", " ", " "], 
            [" ", " ", " "], 
            [" ", " ", " "] ]

class TicTacToe:
    def __init__(self):
        # Initialize the game with the board and current player
      self.__board=initialBoard()
      self.__player=HUMAN

    def __str__(self):
      printstring = "\n" + self.__board[0][0] + '|' + self.__board[0][1] + '|' + self.__board[0][2] +"\n-----\n" + self.__board[1][0] + "|" + self.__board[1][1] + "|" + self.__board[1][2]+"\n-----\n" + self.__board[2][0] + "|" + self.__board[2][1] + "|" + self.__board[2][2] + "\n"
      return(printstring)


    def getPlayer( self ):
        return self.__player

    def isWin(self):
        # See if the board represents a win for the current
        # player. A win is three of the current player's tokens
        # in a single row, column, or either diagonal.
        
        #checkingrows
    
        for i in range (3):
          xcount = 0
          ocount = 0
          for j in range(3):
            if self.__board[i][j] == "X":
              xcount = xcount + 1
            elif self.__board[i][j] == "O":
              ocount = ocount + 1
          if xcount == 3:
            return True
          elif ocount == 3:
            return True

        #checkingcolumn

        for i in range (3):
          xcount = 0
          ocount = 0
          for j in range(3):
            if self.__board[j][i] == "X":
               xcount  =  xcount  + 1
            elif self.__board[j][i] == "O":
              ocount = ocount + 1
          if  xcount  == 3:
            return True
          elif ocount == 3:
            return True


        ocount = 0
        xcount = 0

      #checkingdiagonal
        if (self.__board[0][0] == "X" and self.__board[1][1] == "X" and self.__board[2][2] == "X") or (self.__board[0][2] == "X" and self.__board[1][1] == "X" and self.__board[2][0] == "X"):
             xcount  = 3
        elif (self.__board[0][0] == "O" and self.__board[1][1] == "O" and self.__board[2][2] == "O") or (self.__board[0][2] == "O" and self.__board[1][1] == "O" and self.__board[2][0] == "O"):
             ocount = 3
        if xcount == 3:
          return True
        elif ocount == 3:
          return False


    def swapPlayers( self ):
      #change the current player from HUMAN to MACHINE or vice versa
      if self.__player == HUMAN:
          self.__player  = MACHINE
      else:
          self.__player = HUMAN 
   

    def humanMove( self ):
        # Ask the HUMAN to specify a move.  Check that it's 
        # valid (syntactically, in range, and the space is 
        # not occupied).  Update the board appropriately.
        counter = 100
        gatherinput = input("Your turn:\n  Specify a move r, c: ")
        while counter != 0: #repeat code until r and c are within 0 and 2
          while gatherinput.find(",") == -1: #repeat until comma is not inputted 
            print("Response should be r,c. Try again!")
            gatherinput = input("  Specify a move r, c: ")
            if gatherinput.find(",") != -1:
              r,c = gatherinput.split(",")
              r,c = [int(r), int(c)]
          r,c = gatherinput.split(",")
          r,c = [int(r), int(c)]
          if r > 2 or r < 0 or c > 2 or c < 0: 
            print()
            print("Illegal move specified. Try again!")
            gatherinput = input("  Specify a move r, c: ")

          elif self.__board[r][c] == "X" or self.__board[r][c] == "O":
            print()
            print("Illegal entry. Please chooose an empty slot.")
            gatherinput = input("  Specify a move r, c: ")
          else: 
            self.__board[r][c] = "X"
            TicTacToe.__str__(self)
            counter = 0 



    def machineMove( self ):
        # This is the MACHINE's move.  It picks squares randomly
        # until it finds an empty one. Update the board appropriately.
        # Note: this is a really dumb way to play tic-tac-toe.  
        print("Machine's turn:")
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if self.__board[r][c] == " ":
                print("  Machine chooses: ", r, ", ", c, sep="")
                self.__board[r][c] = "O"
                return
  
def driver( ):
    """This plays tic-tac-toe in a pretty simple-minded
    fashion.  The human player goes first with token "X" and
    alternates with the machine using token "O".  We print
    the board before the first move and after each move."""

    # Print the welcome message
    print( WELCOME )
    # Initialize the board and player
    ttt = TicTacToe()
    print( ttt )
    # There are up to 9 moves in tic-tac-toe.
    for move in range(9):
        # The current player may be HUMAN
        # or MACHINE
        if ttt.getPlayer() == HUMAN:
            # If HUMAN, take a move, print the board,
            # and see if it's a win.
            ttt.humanMove()
            print( ttt )
            if ttt.isWin():
                print( YOU_WON )
                return
        else:
            # Else Machine takes a move.  Print the
            # board and see if the machine won.
            ttt.machineMove()
            print( ttt )
            if ttt.isWin():
                print( YOU_LOST )
                return
        # Swap players.
        ttt.swapPlayers()
    # After nine moves with no winner, it's a tie.
    print( YOU_TIED )

 

driver()
        

