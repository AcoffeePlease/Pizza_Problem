
from file_management import read_file, write_file, score


def main():

    # Read file input
    R, C, L, H, pizza = read_file('original_scenario/example.in')
    #  R, C, L, H, pizza = read_file('original_scenario/small.in')
    #  R, C, L, H, pizza = read_file('original_scenario/medium.in')
    #  R, C, L, H, pizza = read_file('original_scenario/big.in')
    print("R={} , C={} , L={} , H={} , \npizza=\n{} ".format(R, C, L, H, pizza))


    # Pizza_slices creation
    # ( initial X_position, initial Y_position, x_shape, y_shape )
    pizza_slices = []
    pizza_slices.append((0, 0, 3, 2))
    pizza_slices.append((0, 2, 3, 1))
    pizza_slices.append((0, 3, 3, 2))
    print("Pizza slices: {}".format(pizza_slices))

    #Score
    print("Score: {}".format(score(pizza_slices)))

    # Write file output
    write_file("output1.txt", pizza_slices)


if __name__ == '__main__':
    main()
