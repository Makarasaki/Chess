

class Field:

    Field_len = 20

    def __init__(self, X_pos, Y_pos, state):
        self.X_center = X_pos * self.Field_len + self.Field_len/2
        self.Y_center = Y_pos * self.Field_len + self.Field_len/2
        self.X_corner = X_pos * self.Field_len
        self.Y_corner = Y_pos * self.Field_len
        self.state = state


A1 = Field(0, 0, 1)
A2 = Field(0, 1, 1)
A3 = Field(0, 2, 1)
A4 = Field(0, 3, 1)
A5 = Field(0, 4, 1)
A6 = Field(0, 5, 1)
A7 = Field(0, 6, 1)
A8 = Field(0, 7, 1)

B1 = Field(1, 0, 1)
B2 = Field(1, 1, 1)
B3 = Field(1, 2, 1)
B4 = Field(1, 3, 1)
B5 = Field(1, 4, 1)
B6 = Field(1, 5, 1)
B7 = Field(1, 6, 1)
B8 = Field(1, 7, 1)

C1 = Field(2, 0, 0)
C2 = Field(2, 1, 0)
C3 = Field(2, 2, 0)
C4 = Field(2, 3, 0)
C5 = Field(2, 4, 0)
C6 = Field(2, 5, 0)
C7 = Field(2, 6, 0)
C8 = Field(2, 7, 0)

D1 = Field(3, 0, 0)
D2 = Field(3, 1, 0)
D3 = Field(3, 2, 0)
D4 = Field(3, 3, 0)
D5 = Field(3, 4, 0)
D6 = Field(3, 5, 0)
D7 = Field(3, 6, 0)
D8 = Field(3, 7, 0)

E1 = Field(4, 0, 0)
E2 = Field(4, 1, 0)
E3 = Field(4, 2, 0)
E4 = Field(4, 3, 0)
E5 = Field(4, 4, 0)
E6 = Field(4, 5, 0)
E7 = Field(4, 6, 0)
E8 = Field(4, 7, 0)

F1 = Field(5, 0, 0)
F2 = Field(5, 1, 0)
F3 = Field(5, 2, 0)
F4 = Field(5, 3, 0)
F5 = Field(5, 4, 0)
F6 = Field(5, 5, 0)
F7 = Field(5, 6, 0)
F8 = Field(5, 7, 0)

G1 = Field(6, 0, 1)
G2 = Field(6, 1, 1)
G3 = Field(6, 2, 1)
G4 = Field(6, 3, 1)
G5 = Field(6, 4, 1)
G6 = Field(6, 5, 1)
G7 = Field(6, 6, 1)
G8 = Field(6, 7, 1)

H1 = Field(7, 0, 1)
H2 = Field(7, 1, 1)
H3 = Field(7, 2, 1)
H4 = Field(7, 3, 1)
H5 = Field(7, 4, 1)
H6 = Field(7, 5, 1)
H7 = Field(7, 6, 1)
H8 = Field(7, 7, 1)
