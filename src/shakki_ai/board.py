""" 
Vastaa shakkilaudan tilasta ja siirtojen käsittelystä.

Sisältö:
- 8x8lauta
- rivit 0 - 7 (alhaalta ylös)
- sarakkeet 0 - 7 (vasemmalta oikealle)
- Siirtojen suoritus ja peruuttaminen (make/undo)
- Perustoiminnot tilan tarkasteluun (vuorot, pelin päättymisehdot)
"""

BOARD_SIZE = 8

WHITE_PAWN = 1    #sotilas
WHITE_ROOK = 2    #torni
WHITE_KNIGHT = 3  #ratsu
WHITE_BISHOP = 4  #lähetti
WHITE_KING = 5    #kuningas
WHITE_QUEEN = 6   #kuningatar


BLACK_PAWN = -1     #sotilas
BLACK_ROOK = -2     #torni
BLACK_KNIGHT = -3   #ratsu
BLACK_BISHOP = -4   #lähetti
BLACK_KING = -5     #kuningas
BLACK_QUEEN = -6    #kuningatar





class Board():

    def __init__ (self):
        self.board = []
        for i in range(BOARD_SIZE):
            row = []
            for j in range(BOARD_SIZE):
                row.append(0)
            self.board.append(row)

        self.pieces = []
        self.turn = 1
        self._setup_start_pos()


    def _add_piece(self, piece, row, col):
        self.board[row][col] = piece
        self.pieces.append((piece, row, col))

    def _setup_start_pos(self):
        for i in range(BOARD_SIZE): 
            self._add_piece(WHITE_PAWN, 1, i)

        self._add_piece(WHITE_ROOK, 0, 0)
        self._add_piece(WHITE_ROOK, 0, 7)

        self._add_piece(WHITE_KNIGHT, 0, 1)
        self._add_piece(WHITE_KNIGHT, 0, 6)

        self._add_piece(WHITE_BISHOP, 0, 2)
        self._add_piece(WHITE_BISHOP, 0, 5)

        self._add_piece(WHITE_KING, 0, 3)
        self._add_piece(WHITE_QUEEN, 0, 4)

        for i in range(BOARD_SIZE): 
            self._add_piece(BLACK_PAWN, 6, i)

        
        self._add_piece(BLACK_ROOK, 7, 0)
        self._add_piece(BLACK_ROOK, 7, 7)

        self._add_piece(BLACK_KNIGHT, 7, 1)
        self._add_piece(BLACK_KNIGHT, 7, 6)

        self._add_piece(BLACK_BISHOP, 7, 2)
        self._add_piece(BLACK_BISHOP, 7, 5)

        self._add_piece(BLACK_KING, 7, 3)
        self._add_piece(BLACK_QUEEN, 7, 4)



    def in_bounds(self, row, col):
        if 0 <= row <= 7 and 0 <= col <= 7:
            return True
        else:
            return False

    
    def get_piece(self, row, col):
        return self.board[row][col]
    
    def is_empty(self, row, col):
        piece = self.get_piece(row, col)
        if piece == 0:
            return True
        else:
            return False
        

    def is_friend(self, row, col, color):
        piece = self.get_piece(row, col)

        if piece * color > 0:
            return True
        else:
            return False
            
    
    def is_enemy(self, row, col, color):
        piece = self.get_piece(row, col)

        if piece * color < 0:
            return True
        
        else:
            return False


    
    def parse_move(self, text):
        text = text.strip().lower()

        if len(text) != 4:
            print("syötteen täytyy olla neljä merkkiä")
            return None
        
        col1 = text[0]
        row1 = text[1]
        col2 = text[2]
        row2 = text[3]

        if col1 not in "abcdefgh" or col2 not in "abcdefgh":
            print("kirjainten pitää olla välillä a-h")
            return None
        if row1 not in "12345678" or row2 not in "12345678":
            print("Numeroiden pitää olla välillä 1-8")
            return None
        
        c1 = ord(col1) - ord("a")
        c2 = ord(col2) - ord("a")
        r1 = int(row1) - 1
        r2 = int(row2) - 1

        return (r1,c1), (r2,c2)



    def make_move(self, move):
        (r1, c1), (r2, c2) = move 

        previous_turn = self.turn

        if not self.in_bounds(r2, c2) or not self.in_bounds(r1, c1):
            print("Siirron täytyy olla laudalla")
            return None
        
        piece = self.board[r1][c1]

        if piece == 0:
            print("Alkuruutu tyhjä")
            return None
        
        if piece * self.turn <= 0:
            print("Vastustajan nappulaa ei saa siirtää!")
            return None
        
        captured = self.board[r2][c2]

        if captured != 0 and captured * self.turn > 0:
            print("Oma nappula ruudussa")
            return None

        self.board[r2][c2] = piece
        self.board[r1][c1] = 0


        for i, (p, rr, cc) in enumerate(self.pieces):
            if p == piece and rr == r1 and cc == c1:
                self.pieces[i] = (piece, r2, c2)
                break
        
        for i, (p, rr, cc) in enumerate(self.pieces):
            if p == captured and rr == r2 and cc == c2:
                self.pieces.pop(i)
                break


        self.turn *= -1

        move_info = {"from": (r1, c1), 
                    "to": (r2, c2), 
                    "moved_piece": piece, 
                    "captured": captured,
                    "previous_turn": previous_turn}

        return move_info


    

    def undo_move(self, move_info):
        (r1, c1) = move_info["from"]
        (r2, c2) = move_info["to"]
        piece = move_info["moved_piece"]
        captured = move_info["captured"]
        previous_turn = move_info["previous_turn"]


        self.board[r1][c1] = piece 

        if captured == 0:
            self.board[r2][c2] = 0

        else:
            self.board[r2][c2] =  captured

        
        for i, (p, rr, cc) in enumerate(self.pieces):
            if p == piece and rr == r2 and cc == c2:
                self.pieces[i] = (piece, r1, c1)
                break

        if captured != 0:
            self.pieces.append((captured, r2, c2))

        self.turn = previous_turn




    def generate_knight_moves(self, row, col):

        offsets = [(+2, +1), (+2, -1), (-2, +1), (-2, -1), 
                   (+1, +2), (+1, -2), (-1, +2), (-1, -2)] #(dr, dc)
        
        color = self.turn

        moves = []


        for (dr, dc) in offsets:
            new_row = row + dr
            new_col = col + dc

            if not self.in_bounds(new_row, new_col):
                continue

            if self.is_friend(new_row, new_col, color):
                continue

            moves.append(((row, col), (new_row, new_col)))

        return moves



    def generate_pawn_moves(self, row, col):
        piece = self.board[row][col]
        moves = []

        if piece == 0:
            return []

        if piece > 0:  #valkoinen
            dir = +1

        if piece < 0: #musta
            dir = -1


        new_row = row + dir

        if self.in_bounds(new_row, col) and self.is_empty(new_row, col):
            moves.append(((row, col), (new_row, col)))

        return moves


    def generate_bishop_moves(self, row, col):
        piece = self.board[row][col]

        if piece == 0:
            return []
        
        moves = []

        offsets = [(+1, +1), (+1, -1), (-1, +1), (-1, -1)]

        for (dr, dc) in offsets:
            step = 1
            while True:
                new_row = row + (step*dr)
                new_col = col + (step*dc)

                if not self.in_bounds(new_row, new_col):
                    break

                if not self.is_empty(new_row, new_col):
                    break
                
                
            
                moves.append(((row, col), (new_row, new_col)))
                step += 1


        return moves


    def generate_rook_moves(self, row, col):
        piece = self.board[row][col]

        if piece == 0:
            return []
        
        moves = []

        offsets = [(+1, 0), (0, +1), (-1, 0), (0, -1)]

        for (dr, dc) in offsets:
            step = 1
            while True:
                new_row = row + (step*dr)
                new_col = col + (step*dc)

                if not self.in_bounds(new_row, new_col):
                    break

                if not self.is_empty(new_row, new_col):
                    break
                
                
            
                moves.append(((row, col), (new_row, new_col)))
                step += 1


        return moves


    def generate_queen_moves(self, row, col):
        piece = self.board[row][col]

        if piece == 0:
            return []
        
        moves = []

        offsets = [(+1, 0), (0, +1), (-1, 0), (0, -1), (+1, +1), (+1, -1), (-1, +1), (-1, -1)]

        for (dr, dc) in offsets:
            step = 1
            while True:
                new_row = row + (step*dr)
                new_col = col + (step*dc)

                if not self.in_bounds(new_row, new_col):
                    break

                if not self.is_empty(new_row, new_col):
                    break
                
                
            
                moves.append(((row, col), (new_row, new_col)))
                step += 1


        return moves
    
    def generate_king_moves(self, row, col):
        piece = self.board[row][col]

        if piece == 0:
            return []
        
        moves = []

        offsets = [(+1, 0), (0, +1), (-1, 0), (0, -1), (+1, +1), (+1, -1), (-1, +1), (-1, -1)]

        for (dr, dc) in offsets:
            new_row = row + dr
            new_col = col + dc

            if self.in_bounds(new_row, new_col) and self.is_empty(new_row, new_col):
                moves.append(((row, col), (new_row, new_col)))

        return moves
    

    def generate_piece_moves(self, row, col):
        piece = self.board[row][col]

        if piece == 0:
            return []
        
        if abs(piece) == WHITE_PAWN:
            return self.generate_pawn_moves(row, col) 

        elif abs(piece) == WHITE_ROOK:
            return self.generate_rook_moves(row, col) 

        elif abs(piece) == WHITE_KNIGHT:
            return self.generate_knight_moves(row, col) 

        elif abs(piece) == WHITE_BISHOP:
            return self.generate_bishop_moves(row, col)  

        elif abs(piece) == WHITE_KING:
            return self.generate_king_moves(row, col)  

        elif abs(piece) == WHITE_QUEEN:
            return self.generate_queen_moves(row, col) 

        return []
    
    def generate_all_moves(self, color):
        all_moves = []

        for (piece, row, col) in self.pieces:

            if piece * color <= 0:
                continue

            moves_for_this_piece = self.generate_piece_moves(row, col)
            all_moves.extend(moves_for_this_piece)


        return all_moves 

