

class Tablero:
    def __init__(self):
        self.clearboard()

    #Pseudo Getter pero feo, mejor print_board
    @property
    def board(self):
        return self._board
    

    def clearboard(self):
         self._board = [[' ' for _ in range(3)] for _ in range(3)]

   
    def is_take_place(self, fila, col):
        return self._board[fila][col] != ' '
    

    def is_board_full(self):
        return all(cell != ' ' for row in self._board for cell in row)
    
    #Add /Agrega
    def add_movement(self, fila, col, simbolo):
        if self.is_take_place(fila, col):  
            return False
        else:
            self._board[fila][col] = simbolo  
            return True  
        


    def is_game_won(self, symbol):
     
        # Verificar filas y columnas / Check rows and columns
        for i in range(3):
            if all(self._board[i][j] == symbol for j in range(3)) or \
               all(self._board[j][i] == symbol for j in range(3)):
                return True
        
        # Verificar diagonales / Check diagonals
        if all(self._board[i][i] == symbol for i in range(3)) or \
           all(self._board[i][2 - i] == symbol for i in range(3)):
            return True
        
        return False
    

        
    def print_board(self):
        x=0
        print("")
        for row in self._board:
            x=x+1
            print('|'.join(row))
            if (x!=3):
                print("-----")



    