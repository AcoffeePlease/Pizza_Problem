from file_management import read_file, write_file


def main():
    R, C, L, H, pizza = read_file('original_scenario/example.in')
    #  R, C, L, H, pizza = read_file('original_scenario/small.in')
    #  R, C, L, H, pizza = read_file('original_scenario/medium.in')
    #  R, C, L, H, pizza = read_file('original_scenario/big.in')

    print("R={} , C={} , L={} , H={} , \npizza=\n{} ".format(R, C, L, H, pizza))




if __name__ == '__main__':
    main()
