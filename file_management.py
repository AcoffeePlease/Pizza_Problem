import numpy as np

"""
  Leggere file input di questo formato
  3 5 1 6
  TTTTT
  TMMMT
  TTTTT
"""
def read_file(filename):
    lines = open(filename).readlines()
    R, C, L, H = [int(val) for val in lines[0].split()]
    pizza = np.array(
        [list(map(lambda item: 1 if item == 'T' else 0, row.strip()))
         for row in lines[1:]])
    return R, C, L, H, pizza


"""
  Scrivere file output con questo formato
  3
  0 0 2 1
  0 2 2 2
  0 3 2 4
"""
def write_file(filename, pizza_slices):
    with open(filename, 'w') as f:
        f.write(f"{len(pizza_slices)}\n")
        for slice in pizza_slices:
            r, c, dr, dc = slice
            f.write(f"{r} {c} {r + dr - 1} {c + dc - 1}\n")



