def print_Board (board):
    for i in range (9):
        print (board[i], end=" ")
        if (((i+1)%3)==0): 
            print ()
    print ()
    return True

def vin_Cond (board):
    ## горизонтальные линии
    if(board[0] == board[1] == board[2]):
        if(board[0] == "X"):
            return (1)
        else:
            return (2)
    if(board[3] == board[4] == board[5]):
        if(board[3] == "X"):
            return (1)
        else:
            return (2)
    if(board[6] == board[7] == board[8]):
        if(board[6] == "X"):
            return (1)
        else:
            return (2)
    ## Вертикальные линии
    if(board[0] == board[3] == board[6]):
        if(board[0] == "X"):
            return (1)
        else:
            return (2)
    if(board[1] == board[4] == board[7]):
        if(board[1] == "X"):
            return (1)
        else:
            return (2)
    if(board[2] == board[5] == board[8]):
        if(board[0] == "X"):
            return (1)
        else:
            return (2)
    ## Диагонали
    if(board[0] == board[4] == board[8]):
        if(board[0] == "X"):
            return (1)
        else:
            return (2)
    if(board[2] == board[4] == board[6]):
        if(board[2] == "X"):
            return (1)
        else:
            return (2)
    return (0)


board = [1,2,3,4,5,6,7,8,9]
i=1
temp = 0
while (vin_Cond(board)==0 and i < 10):
    print_Board(board)
    if(i%2==1):
        temp = int(input ("Ход X\n"))
    else:
        temp = int(input ("Ход O\n"))
    while(temp > 9 or temp < 1 or board[temp-1] == "X" or board[temp-1] == "O"):
            print("Ошибка\n")
            print_Board(board)
            if(i%2==1):
                temp = int(input ("Ход X\n"))
            else:
                temp = int(input ("Ход O\n"))
    if(i%2==1):
        board[temp-1] = "X"
    else:
        board[temp-1] = "O"
    i+=1
print_Board(board)
if(vin_Cond(board)==0):
    print ("Ничья")
elif(vin_Cond(board)==1):
    print ("Выйграл X")
else:
    print ("Выйграл O")
    