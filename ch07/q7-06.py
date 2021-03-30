from random import randint


class piece():
    def __init__(self, data, x, y):
        self.data = data
        self.x = x
        self.y = y
        self.type = ['corner', 'edge', 'inner']


class JigsawPuzzle():
    def __init__(self, n, pieces):
        self.size = n
        self.board = [[piece(0, x, y) for y in range(n)] for x in range(n)]
        self.pieces = []
        self.matches = {} #


    def load_jigsaw(self, matrix):
        for row in matrix:
            for column in row:
                self.pieces = (row, column)

    def is_match(self, piece1, piece2):
        return randint(0, 1)

    def add_match(self, piece1, piece2):
        self.matches.setdefault(piece1, []).append(piece2)
        self.matches.setdefault(piece2, []).append(piece1)

    def is_piece_neiborghs_complete(self, piece):
        if piece.type == 'corner' and self.matches.get(piece, None) == 2:
            return True


    # O(n^2)
    def resolve_puzzle(self):
        # Is there any type of ordering n log(n)
        
        for piece in pieces:
            if is_piece_neiborghs_complete(piece):
                break
            for i in range(len(pieces)):
                if piece(is_match(piece, pieces[i])):
                    add_match(piece, piece)
                if is_piece_neiborghs_complete(piece):
                    break ## double break

        # build the board
        # Find Corners
        # find neibors




