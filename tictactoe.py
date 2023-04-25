import time
import os

def print_board(boardState):
    print("-------------")
    for i in range(3):
        print("| ", end='')
        for j in range(3):
            print(str(boardState[i*3+j]) + " | ", end='')
        print()
        print("-------------")
            
    return

def check_win(boardState):
    if (boardState[0] == boardState[4] and boardState[0] == boardState[8] and boardState[0] != ' '):
        print()
        print(str(boardState[0]) + " wins!")
        return True

    if (boardState[2] == boardState[4] and boardState[2] == boardState[6] and boardState[2] != ' '):
        print()
        print(str(boardState[0]) + " wins!")
        return True

    for i in range(3):
        if (boardState[i] == boardState[i+3] and boardState[i] == boardState[i+6] and boardState[i] != ' '):
            print()
            print(str(boardState[i]) + " wins!")
            return True
        
        if (boardState[i*3] == boardState[i*3+1] and boardState[i*3] == boardState[i*3+2] and boardState[i*3] != ' '):
            print()
            print(str(boardState[i*3]) + " wins!")
            return True

    return False

def main():
    boardState = [' ']*9
    
    boardOccupied = [False]*9
    
    displayBoard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    curTurn = 'X'
    
    while (True):
        os.system('cls')
        print("For turn reference:")
        print_board(displayBoard)
        print("\n\n")
        print_board(boardState)

        if (check_win(boardState)):
            break

        if (curTurn == 'X'):
            inp = int(input("X's Turn: "))
        else:
            inp = int(input("O's Turn: "))

        if ((inp > 9) or (inp < 1) or boardOccupied[inp-1]):
            print("Please input valid turn")
            time.sleep(2)
            continue

        boardOccupied[inp-1] = True
        boardState[inp-1] = curTurn

        if (curTurn == 'X'):
            curTurn = 'O'
        else:
            curTurn = 'X'

if __name__ == "__main__":
    main()

        

