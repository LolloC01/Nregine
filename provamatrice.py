import numpy as np

chess = []
for x in range(8):
    c = []
    for y in range(8):
        c.append(y)
    chess.append(c)
for x in chess:
    print(x)