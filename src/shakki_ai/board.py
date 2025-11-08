""" 
Vastaa shakkilaudan tilasta ja siirtojen käsittelystä.

Sisältö:
- 8x8lauta
- Siirtojen suoritus ja peruuttaminen (make/undo)
- Perustoiminnot tilan tarkasteluun (vuorot, pelin päättymisehdot)

"""

class Board():

    def __init__ (self):
        self.board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ]

        self.turn = "Black"  #Musta aloittaa pelin 

    def render(self):
        for i, row in enumerate(self.board): # Käy läpi laudan rivit
            print(8-i," ".join(row)) #Tulostaa rivin numeron ja laudan rivin
        print("  a b c d e f g h")  #Tulostaa sarakkeiden kirjaimet

    def get_piece(self, row, col): #Hakee nappulan ruudusta
        return self.board[row][col]
    
    def parse_move():
