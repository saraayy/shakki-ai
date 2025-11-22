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

        self.turn = "white"  

    def render(self):
        for i, row in enumerate(self.board): # Käy läpi laudan rivit
            print(8-i," ".join(row)) 
        print("  a b c d e f g h")  

    def get_piece(self, row, col): #Hakee nappulan ruudusta
        return self.board[row][col]
    
    def parse_move(self, text):
        text = text.strip()

        col_1 = text[0]
        row_1 = text[1]
        col_2 = text[2]
        row_2 = text[3]


        if len(text) != 4:
            raise ValueError("Siirron pitää olla muodossa 'e2e4' ")

        if col_1 not in  "abcdefgh" and col_2 not in "abcdefgh":
            raise ValueError("Sarakkeen pitää olla a-h")
        
        if row_1 not in "12345678" and row_2 not in "12345678":
            raise ValueError("Rivin pitää olla 1-8")
        

        col_1_idx = ord(col_1) - ord('a')
        col_2_idx = ord(col_2) - ord('a')

        row_1_idx = 8 - int(row_1)
        row_2_idx = 8 - int(row_2)

        return (row_1_idx, col_1_idx), (row_2_idx, col_2_idx)
    
    def in_bounds(self, row, col): 
        
        if row in range(0,8) and col in range(0,8):
            return True
        else: 
            return False


    def piece_color(self, piece): 
        
        if piece == ".":
            return None
        elif piece.isupper():
            return "white"
        elif piece.islower():
            return "black"
        else:
            return None


    def color_at(self, row, col):
        if self.in_bounds(row, col): 
            return self.piece_color(self.board[row][col])

        else:
            return None

        
    def is_empty(self, row, col):
        if not self.in_bounds(row, col):
            return False
        piece = self.board[row][col]
        if piece == ".":
            return True
        else:
             return False


    def is_friend(self, row, col, color):
        if not self.in_bounds(row, col):
            return False
        
        square_color = self.color_at(row, col)
        if square_color is None:
            return False

        return square_color == color
            
    
    def is_enemy(self, row, col, color):
        if not self.in_bounds(row, col):
            return False
            
        square_color = self.color_at(row, col)
        if square_color is None:
            return False

        return square_color != color



    def make_move(self, move):
        (r1, c1), (r2,c2) = move

        if not self.in_bounds(r1,c1) or not self.in_bounds(r2,c2):
            raise ValueError("Siirto laudan ulkopuolella")

        piece = self.get_piece(r1,c1)

        if piece == ".":
            raise ValueError("Alkuruutu on tyhjä")
        
        piece_color = self.piece_color(piece)

        if piece_color != self.turn:
            raise ValueError ("Et voi siirtää vastustajan nappulaa") 
        
        target = self.board[r2][c2]

        if target == ".":
            captured_piece = None
            
        elif target != ".":
            captured_piece = target

        self.board[r2][c2] = piece
        self.board[r1][c1] = "."

        previous_turn = self.turn

        if self.turn == "black":
            self.turn = "white"

        elif self.turn == "white":
            self.turn = "black"

        move_info = {
            "from": (r1, c1),
            "to": (r2, c2),
            "moved_piece": piece,
            "captured_piece": captured_piece,
            "previous_turn": previous_turn
            }
        
        return move_info


    def undo_move(self, info):
        r1, c1 = info["from"]
        r2, c2 = info["to"]
        previous_turn = info["previous_turn"]
        moved_piece = info["moved_piece"]
        captured_piece = info["captured_piece"]

        self.board[r1][c1] = moved_piece

        if captured_piece == None:
            self.board[r2][c2] = "."

        else:
            self.board[r2][c2] = captured_piece 

        self.turn = previous_turn

    def generate_moves_for_square(self, row, col):
        piece = self.get_piece(row, col)

        if piece == ".":
            return []
        
        piece_type = piece.upper()
        color = self.piece_color(piece)

        if color != self.turn:
            return []
        
        if piece_type == "N":
            return self._knight_moves(row, col, color)

        else:
            return []
        
    
    def _knight_moves(self, row, col, color):
        moves = []
        offsets = [
            (+2, +1), (+2, -1), (-2, +1), (-2, -1), 
            (+1, +2), (+1, -2), (-1, +2), (-1, -2)
        ]
        for dr, dc in offsets:
            new_row = row + dr
            new_col = col + dc

            if not self.in_bounds(new_row, new_col):
                continue

            if self.is_friend(new_row, new_col, color):
                continue

            moves.append(((row, col), (new_row, new_col)))
            

        return moves
        

        



