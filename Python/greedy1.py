import numpy as np
from numpy import random

from file_management import read_file, write_file, score


# Boolean function return true if there is an available space
def space(slice_mask, R, C):
    for righe in R:
        for colonne in C:
            if slice_mask(righe, colonne) == 0:
                return True
    return False


# Boolean function return true if respect:
#  at least L mushrooms
#  at least L tomotoes
#  total area of each slice must be at most H
def costraints(riga, colonna, shape, H, L, pizza):
    if shape[0] * shape[1] > H:
        return False

    sum_tomotoes = 0
    sum_mushrooms = 0
    for x in range(riga, riga + shape[0]):
        for y in range(colonna, colonna + shape[1]):
            if pizza[x, y] == 0:
                sum_mushrooms += 1
            else:
                sum_tomotoes += 1

    if sum_mushrooms < L or sum_tomotoes < L:
        return False

    return True


#  Random shape and random point of init
def main():
    # Read file input
    R, C, L, H, pizza = read_file('original_scenario/example.in')
    #  R, C, L, H, pizza = read_file('original_scenario/small.in')
    #  R, C, L, H, pizza = read_file('original_scenario/medium.in')
    #  R, C, L, H, pizza = read_file('original_scenario/big.in')
    print("R={} , C={} , L={} , H={} , \npizza=\n{} ".format(R, C, L, H, pizza))

    possible_shapes = [(4, 2), (2, 4), (3, 3), (5, 2), (2, 5), (11, 1), (1, 11),
                       (2, 6), (6, 2), (3, 4), (4, 3)]
    slice_mask = np.zeros_like(
        pizza)  # stores the sliced cells as 1 for easy lookup

    # Slices of pizza
    # ( initial X_position, initial Y_position, x_shape, y_shape )
    pizza_slices = []

    i = 0
    while i < 20000:

        #  choose a random position in slice_mask
        found1 = False
        riga = 0
        colonna = 0
        while found1 == False and space(slice_mask):
            riga = random.randint(0, R)
            colonna = random.randint(0, C)
            if slice_mask[riga, colonna] == 0:
                found1 = True

        #  choose a random shape
        shape = possible_shapes(random.randint(0, 10))

        # test if respect costraints
        if costraints(riga, colonna, shape, H, L, pizza):
            #  Inserisci in slice_mask che è stata presa
            for x in range(riga, riga + shape[0]):
                for y in range(colonna, colonna + shape[1]):
                    slice_mask[x, y] = 1
            #  Inserisci la fetta di pizza tagliata
            pizza_slices.append(riga, colonna, shape[0], shape[1])

        i = i + 1

    print("Pizza slices: {}".format(pizza_slices))

    # Score
    print("Score: {}".format(score(pizza_slices)))

    # Write file output
    write_file("output1.txt", pizza_slices)


if __name__ == '__main__':
    main()
