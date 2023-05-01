import numpy as np
import os
import random
import time





ROW_COUNT=9
COL_COUNT=9

#Creating the game board.
def create_board():
    board = np.zeros((ROW_COUNT,COL_COUNT),dtype=int)
    return board

#Droping the piece
def drop_piece(board,row,col,piece):
    board[row][col]=piece;



#Checking the move is for legal.
def is_valid_choice(board,col):
    for i in range(ROW_COUNT):
        if board[ROW_COUNT-1][col]==0:
            return True
    return False


#Checking the column that piece will be stayed.
def get_column(board,col):
    for i in range(ROW_COUNT):
        if board[i][col]==0:
            return i


#Printing the board
def print_board(board):
    print(np.flip(board,0)) 

#Checking the winning move
def winning(board,piece):

    #Checking for vertically
    for i in range(COL_COUNT):
        for j in range(ROW_COUNT-3):
            if board[j][i]== piece and board[j+1][i]== piece and board[j+2][i]== piece and board[j+3][i]== piece:
                return True
            
    #Checking for horizontally
    for i in range(COL_COUNT-3):
        for j in range(ROW_COUNT):
            if board[j][i]== piece and board[j][i+1]== piece and board[j][i+2]== piece and board[j][i+3]== piece:
                return True
            
    #Checking for right diagonal
    for i in range(COL_COUNT-3):
        for j in range(ROW_COUNT-3):
            if board[j][i]== piece and board[j+1][i+1]== piece and board[j+2][i+2]== piece and board[j+3][i+3]== piece:
                return True
            
    #Checking for left diagonal
    for i in range(COL_COUNT-3):
        for j in range(3,ROW_COUNT):
            if board[j][i]== piece and board[j-1][i+1]== piece and board[j-2][i+2]== piece and board[j-3][i+3]== piece:
                return True
            

    return False



#Writing board to the txt file 
def write_tahta_txt(board):
    # Dosyayı yazma modunda açma
    with open("Tahta.txt", "w") as f:
        # Her satıra bir dizi elemanı yazdırma
        for row in board:
            f.write("   ".join(str(eleman) for eleman in row) + "\n\n")



#Getting previous game's board
def get_tahta_txt():
    # Metin dosyasını okuma modunda açma
    with open("Tahta.txt", "r") as f:
        # Her satırı bir diziye dönüştürme ve ana diziye ekleme
        board = []
        for i in f:
            i = i.strip().split() # Satırdaki elemanları boşluklardan ayırma
            if i:
                board.append([int(eleman) for eleman in i]) # Her elemanı tam sayıya dönüştürme ve ana diziye ekleme
        
        return(np.flip(board,0))


#Saves the turn value for the next game
def save_turn(turn):
    with open("Hamle.txt","a") as f:
        word="\nTurn="+str(turn)
        f.write(word)



#Getting the turn value for the continue to the previous game.
def get_turn():
    with open("Hamle.txt", "r") as f:
        for line in f:
            for word in line.split():

                if "Turn=" in line:
                    turn_index = line.index("Turn=") + len("Turn=")
                    turn_str = line[turn_index:].strip()
                    if turn_str:
                        turn = int(turn_str)
                       
                        return turn
                
                    
        

def write_hamle_txt(row,col,piece):
    with open("Hamle.txt","a")as f:
        move="\nPLAYER "+str(piece)+" -> "+str(row+1)+str(col+1)+"\n"
        f.write(move)
    


def head_tail():
    list=["Head","Tail"]
    time.sleep(0.5)
    print("Decisioning...")
    time.sleep(0.5)
    print(random.choice(list),"is Player 1")

    




board=[]
game_over=False


choice=int(input("Make a choice: \n 1)Play new game \n 2)Continue a previous game \n "))
if choice==1:
    print("\n\n\n****** WELCOME TO THE CONNECT 4 ******\n PLAYER 1 IS YELLOW, PLAYER 2 IS RED.\n MAKE YOUR GUESS FOR HEAD AND TAIL. ")
    time.sleep(5)
    head_tail()
    board=create_board()
    turn=0
    if os.path.exists("Hamle.txt"):
        os.remove("Hamle.txt")

elif choice==2:
    board=get_tahta_txt()
    turn=get_turn()

else:
    print("You did invalid choice...")


while not game_over:
    

    print_board(board)
    if turn%2==0:
        #Player 1 will make a move.
        col=int(input("Player 1 make your move (0 is first, 8 is last column, 9 for save and exit.) : "))
        
        if col==9:
            write_tahta_txt(np.flip(board,0))
            save_turn(turn)
            game_over=True


        elif (col>=0 and col<9):
            
            if is_valid_choice(board,col):
                row=get_column(board,col)
                drop_piece(board,row,col,1)
                write_tahta_txt(np.flip(board,0))
                write_hamle_txt(row,col,1)
                

                if winning(board,1)==True:
                    print("1st Player WON")
                    game_over=True
            else:
                print("You can not drop a piece here...")
                turn -=1
        else:
            print("You entered invalid value..")
            break
        

    else:
        #Player 2 will make a move.
        col=int(input("Player 2 make your move (0 is first, 8 is last column, 9 for save and exit.) : "))
        
        if col==9:
            write_tahta_txt(np.flip(board,0))
            save_turn(turn)
            game_over=True


        elif (col>=0 and col<9):

            if is_valid_choice(board,col):
                row=get_column(board,col)
                drop_piece(board,row,col,2)
                write_tahta_txt(np.flip(board,0))
                write_hamle_txt(row,col,2)
                
                
                if winning(board,2)==True:
                    print("2nd Player WON")
                    game_over=True
            else:
                print("You can not drop a piece here...")
                turn-=1

        else:
            print("You entered invalid value..")
            break

    

    turn +=1
    


    #Checking draw situation
    if turn==80:
        print("DRAW, GAME IS FINISHED...")
    