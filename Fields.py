class Field:

    # legal = 0
    Field_len = 47
    offset_X = 5 - ((Field_len - 10)/2)
    offset_Y = 35
    # jump_offset = 0
    X_dump = 8 * Field_len + offset_X - 15
    Y_dump = 4 * Field_len + offset_Y

    def __init__(self, X_pos, Y_pos, state):
        self.X_center = X_pos * self.Field_len + self.Field_len/2 + self.offset_X
        self.Y_center = Y_pos * self.Field_len + self.Field_len/2 + self.offset_Y
        self.X_corner = X_pos * self.Field_len + self.offset_X if X_pos > 6 else (X_pos + 1) * \
            self.Field_len + self.offset_X
        # self.X_corner = self.X_center + self.Field_len/2
        self.Y_corner = Y_pos * self.Field_len + self.offset_Y if Y_pos > 3 else (Y_pos + 1) * \
            self.Field_len + self.offset_Y  # było > 4 (tak jakby co xD)
        self.state = state
        self.X_pos = X_pos
        self.Y_pos = Y_pos
        # self.X_dump = 8 * self.Field_len + self.offset_X - 15
        # self.Y_dump = 4 * self.Field_len + self.offset_Y

        self.X_outside = X_pos * self.Field_len + self.offset_X if X_pos < 4 else (X_pos + 1) * \
            self.Field_len + self.offset_X
        self.Y_outside = Y_pos * self.Field_len + self.offset_Y if Y_pos < 4 else (Y_pos + 1) * \
            self.Field_len + self.offset_Y
        # FOR HORSES
        self.X_corner_R = self.X_center + self.Field_len/2
        self.X_corner_L = self.X_center - self.Field_len/2
        self.Y_corner_U = self.Y_center + self.Field_len/2
        self.Y_corner_D = self.Y_center - self.Field_len/2


all_fields = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8",
              "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
              "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
              "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8",
              "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8",
              "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
              "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8",
              "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]

a1 = Field(0, 0, 'R')
a2 = Field(0, 1, 'P')
a3 = Field(0, 2, '0')
a4 = Field(0, 3, '0')
a5 = Field(0, 4, '0')
a6 = Field(0, 5, '0')
a7 = Field(0, 6, 'p')
a8 = Field(0, 7, 'r')

b1 = Field(1, 0, 'N')
b2 = Field(1, 1, 'P')
b3 = Field(1, 2, '0')
b4 = Field(1, 3, '0')
b5 = Field(1, 4, '0')
b6 = Field(1, 5, '0')
b7 = Field(1, 6, 'p')
b8 = Field(1, 7, 'n')

c1 = Field(2, 0, 'B')
c2 = Field(2, 1, 'P')
c3 = Field(2, 2, '0')
c4 = Field(2, 3, '0')
c5 = Field(2, 4, '0')
c6 = Field(2, 5, '0')
c7 = Field(2, 6, 'p')
c8 = Field(2, 7, 'b')

d1 = Field(3, 0, 'Q')
d2 = Field(3, 1, 'P')
d3 = Field(3, 2, '0')
d4 = Field(3, 3, '0')
d5 = Field(3, 4, '0')
d6 = Field(3, 5, '0')
d7 = Field(3, 6, 'p')
d8 = Field(3, 7, 'q')

e1 = Field(4, 0, 'K')
e2 = Field(4, 1, 'P')
e3 = Field(4, 2, '0')
e4 = Field(4, 3, '0')
e5 = Field(4, 4, '0')
e6 = Field(4, 5, '0')
e7 = Field(4, 6, 'p')
e8 = Field(4, 7, 'k')

f1 = Field(5, 0, 'B')
f2 = Field(5, 1, 'P')
f3 = Field(5, 2, '0')
f4 = Field(5, 3, '0')
f5 = Field(5, 4, '0')
f6 = Field(5, 5, '0')
f7 = Field(5, 6, 'p')
f8 = Field(5, 7, 'b')

g1 = Field(6, 0, 'N')
g2 = Field(6, 1, 'P')
g3 = Field(6, 2, '0')
g4 = Field(6, 3, '0')
g5 = Field(6, 4, '0')
g6 = Field(6, 5, '0')
g7 = Field(6, 6, 'p')
g8 = Field(6, 7, 'n')

h1 = Field(7, 0, 'R')
h2 = Field(7, 1, 'P')
h3 = Field(7, 2, '0')
h4 = Field(7, 3, '0')
h5 = Field(7, 4, '0')
h6 = Field(7, 5, '0')
h7 = Field(7, 6, 'p')
h8 = Field(7, 7, 'r')


def msg_gen(X_pos_mm, Y_pos_mm, M_state):
    return "X{} Y{} M{} ".format(X_pos_mm, Y_pos_mm, M_state)
