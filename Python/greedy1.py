import numpy as np
import random

from file_management import read_file, write_file, score


# Boolean function return true if there is an available space
def space(slice_mask, R, C):
    for righe in range(R):
        for colonne in range(C):
            if slice_mask[righe, colonne] == 0:
                return True
    return False


# Boolean function return true if respect:
#  at least L mushrooms
#  at least L tomotoes
def count_food(riga, colonna, shape, L, pizza):
    sum_tomotoes = 0
    sum_mushrooms = 0
    for x in range(riga, riga + shape[0]):
        for y in range(colonna, colonna + shape[1]):
            if pizza[x, y] == 0:
                sum_mushrooms += 1
            else:
                sum_tomotoes += 1
    print("sum_mushrooms {} sum_tomaoes {}".format(sum_mushrooms,
                                                   sum_tomotoes))
    if sum_mushrooms < L or sum_tomotoes < L:
        return False

    return True


#  Random shape and random point of init
def main():
    # Read file input
    #  R, C, L, H, pizza = read_file('original_scenario/example.in')
    #  R, C, L, H, pizza = read_file('original_scenario/small.in')
    R, C, L, H, pizza = read_file('original_scenario/medium.in')
    #  R, C, L, H, pizza = read_file('original_scenario/big.in')
    #  print("R={} , C={} , L={} , H={} , \npizza=\n{} ".format(R, C, L, H, pizza))

    possible_shapes = [(4, 2), (2, 4), (3, 3), (5, 2), (2, 5), (11, 1), (1, 11),
                       (2, 6), (6, 2), (3, 4), (4, 3)]

    slice_mask = np.zeros_like(pizza)
    # stores the sliced cells as 1 and 0 for untouched

    # Slices of pizza
    # ( initial X_position, initial Y_position, x_shape, y_shape )
    pizza_slices = []

    i = 0
    while i < 2 and space(slice_mask, R, C):

        #  choose a random position in slice_mask
        found1 = False
        riga = 0
        colonna = 0
        while not found1 and space(slice_mask, R, C):
            riga = random.randint(0, R - 1)
            colonna = random.randint(0, C - 1)
            if slice_mask[riga, colonna] == 0:
                found1 = True
                print("Riga {} Colonna {}".format(riga, colonna))


        #  choose a random shape
        dimension = False
        while not dimension:
            shape = possible_shapes[random.randint(0, 10)]
            if shape[0] * shape[1] <= H:
                dimension = True
                print(shape)

        # test if respect costraints
        if count_food(riga, colonna, shape, L, pizza):
            #  Inserisci in slice_mask che è stata presa
            for x in range(riga, riga + shape[0]):
                for y in range(colonna, colonna + shape[1]):
                    slice_mask[x, y] = 1
            #  Inserisci la fetta di pizza tagliata
            # TODO
            #pizza_slices.append(riga, colonna, shape[0], shape[1])

        i = i + 1

    print("Pizza slices: {}".format(pizza_slices))

    # Score
    print("Score: {}".format(score(pizza_slices)))

    # Write file output
    write_file("output1.txt", pizza_slices)


if __name__ == '__main__':
    main()
