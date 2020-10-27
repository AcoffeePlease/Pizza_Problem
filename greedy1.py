
from file_management import read_file, write_file


def main():

    # Read file input
    R, C, L, H, pizza = read_file('original_scenario/example.in')
    #  R, C, L, H, pizza = read_file('original_scenario/small.in')
    #  R, C, L, H, pizza = read_file('original_scenario/medium.in')
    #  R, C, L, H, pizza = read_file('original_scenario/big.in')
    print("R={} , C={} , L={} , H={} , \npizza=\n{} ".format(R, C, L, H, pizza))






    # Write file output
    pizza_slices = []
    pizza_slices.append((0, 0, 2, 1))
    pizza_slices.append((0, 2, 2, 2))
    pizza_slices.append((0, 3, 2, 4))
    print(pizza_slices)
    write_file("output1.txt", pizza_slices)


if __name__ == '__main__':
    main()
