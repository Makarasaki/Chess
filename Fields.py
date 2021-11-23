

class Field:

    Field_len = 4

    def __init__(self, X_pos, Y_pos, state):
        self.X_center = X_pos * self.Field_len + self.Field_len/2
        self.Y_center = Y_pos * self.Field_len + self.Field_len/2
        self.X_corner = X_pos * self.Field_len
        self.Y_corner = Y_pos * self.Field_len
        self.state = state
        self.X_dump = 8*self.Field_len
        self.Y_dump = 4*self.Field_len


all_fields = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
              "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",
              "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8",
              "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8",
              "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8",
              "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8",
              "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8",
              "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"]

A1 = Field(0, 0, 1)
A2 = Field(0, 1, 1)
A3 = Field(0, 2, 0)
A4 = Field(0, 3, 0)
A5 = Field(0, 4, 0)
A6 = Field(0, 5, 0)
A7 = Field(0, 6, 1)
A8 = Field(0, 7, 1)

B1 = Field(1, 0, 1)
B2 = Field(1, 1, 1)
B3 = Field(1, 2, 0)
B4 = Field(1, 3, 0)
B5 = Field(1, 4, 0)
B6 = Field(1, 5, 0)
B7 = Field(1, 6, 1)
B8 = Field(1, 7, 1)

C1 = Field(2, 0, 1)
C2 = Field(2, 1, 1)
C3 = Field(2, 2, 0)
C4 = Field(2, 3, 0)
C5 = Field(2, 4, 0)
C6 = Field(2, 5, 0)
C7 = Field(2, 6, 1)
C8 = Field(2, 7, 1)

D1 = Field(3, 0, 1)
D2 = Field(3, 1, 1)
D3 = Field(3, 2, 0)
D4 = Field(3, 3, 0)
D5 = Field(3, 4, 0)
D6 = Field(3, 5, 0)
D7 = Field(3, 6, 1)
D8 = Field(3, 7, 1)

E1 = Field(4, 0, 1)
E2 = Field(4, 1, 1)
E3 = Field(4, 2, 0)
E4 = Field(4, 3, 0)
E5 = Field(4, 4, 0)
E6 = Field(4, 5, 0)
E7 = Field(4, 6, 1)
E8 = Field(4, 7, 1)

F1 = Field(5, 0, 1)
F2 = Field(5, 1, 1)
F3 = Field(5, 2, 0)
F4 = Field(5, 3, 0)
F5 = Field(5, 4, 0)
F6 = Field(5, 5, 0)
F7 = Field(5, 6, 1)
F8 = Field(5, 7, 1)

G1 = Field(6, 0, 1)
G2 = Field(6, 1, 1)
G3 = Field(6, 2, 0)
G4 = Field(6, 3, 0)
G5 = Field(6, 4, 0)
G6 = Field(6, 5, 0)
G7 = Field(6, 6, 1)
G8 = Field(6, 7, 1)

H1 = Field(7, 0, 1)
H2 = Field(7, 1, 1)
H3 = Field(7, 2, 0)
H4 = Field(7, 3, 0)
H5 = Field(7, 4, 0)
H6 = Field(7, 5, 0)
H7 = Field(7, 6, 1)
H8 = Field(7, 7, 1)


def msg_gen(X_pos, Y_pos, M_state):
    return "X{} Y{} M{}".format(X_pos, Y_pos, M_state)
