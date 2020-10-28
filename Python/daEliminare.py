from file_management import read_file, write_file, score
import numpy as np
import random


def space(slice_mask, R, C):
    for righe in range(R):
        for colonne in range(C):
            if slice_mask[righe, colonne] == 0:
                return True
    return False

# Boolean function return true if respect:
#  at least L mushrooms
#  at least L tomotoes
#  total area of each slice must be at most H
def count_food(riga, colonna, shape, L, pizza):
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


def main():

    R, C, L, H, pizza = read_file('original_scenario/medium.in')
    slice_mask = np.zeros_like(pizza)

    pizza_slices = []
    possible_shapes = [(4, 2), (2, 4), (3, 3), (5, 2), (2, 5), (11, 1), (1, 11),
                       (2, 6), (6, 2), (3, 4), (4, 3)]

    i = 0
    while i < 2 and space(slice_mask, R, C):

        #  choose a random position in slice_mask
        found1 = False
        riga = 0
        colonna = 0
        while found1 == False and space(slice_mask, R, C):
            riga = random.randint(0, R-1)
            colonna = random.randint(0, C-1)
            if slice_mask[riga, colonna] == 0:
                found1 = True
                print("Riga {} Colonna {}".format(riga, colonna))

        i = i + 1

        #  choose a random shape
        dimension = False
        while not dimension:
            shape = possible_shapes[random.randint(0, 10)]

            if shape[0]*shape[1] <= H:
                dimension = True
                print(shape)


        sum_tomotoes = 0
        sum_mushrooms = 0
        for x in range(riga, riga+shape[0]):
            for y in range(colonna, colonna+shape[1]):
                if pizza[x, y] == 0:
                    sum_mushrooms += 1
                else:
                    sum_tomotoes += 1
        print("sum_mushrooms {} sum_tomaoes {}".format(sum_mushrooms, sum_tomotoes))

        """
        # test if respect costraints
        if count_food(riga, colonna, shape, L, pizza):
            #  Inserisci in slice_mask che è stata presa
            for x in range(riga, riga + shape[0]):
                for y in range(colonna, colonna + shape[1]):
                    slice_mask[x, y] = 1
            #  Inserisci la fetta di pizza tagliata
            pizza_slices.append(riga, colonna, shape[0], shape[1])
        
        """

if __name__ == '__main__':
    main()
