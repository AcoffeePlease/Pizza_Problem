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
#  TODO: write file output
def write_file(filename):
    out_file = open("output.txt", "w")
    x = 52
    out_file.write(str(x))
    out_file.close()

def main():
    R, C, L, H, pizza = read_file('input.txt')
    print("R={} , C={} , L={} , H={} , \npizza=\n{} ".format(R, C, L, H, pizza))




if __name__ == '__main__':
    main()
