"""
Vastaa tekoälyn päätöksenteosta.

Sisältö:
- minmax (valitsee siirron annettulla syvyydellä)
- alpha-beta karsinta 
- heuristinen arviointi (materiaalipohjainen)

"""


from shakki_ai.board import (
    WHITE_PAWN,
    WHITE_KNIGHT,
    WHITE_BISHOP,
    WHITE_QUEEN,
    WHITE_KING,
    WHITE_ROOK
)


def piece_value(piece):
    p = abs(piece)

    if p == WHITE_PAWN:
        return 1
    
    elif p == WHITE_KNIGHT:
        return 3
    
    elif p == WHITE_BISHOP:
        return 3
    
    elif p == WHITE_ROOK:
        return 5
    
    elif p == WHITE_QUEEN:
        return 9
    
    elif p == WHITE_KING:
        return 100
    
    else:
        return 0
    

def evaluate(board):
    score = 0.0

    for piece, row, col in board.pieces:
        value = piece_value(piece)

        if piece < 0:
            score -= value


        elif piece > 0:
            score += value

        if 2 <= row <= 5 and 2 <= col <= 5:
            center_bonus = 0.1 
            if piece < 0:
                score -= center_bonus

            elif piece > 0:
                score += center_bonus

    
    return score


def choose_move(board):
    color = board.move

    moves = board.generate_all_moves(color)

    if not moves:
        return None
