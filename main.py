import numpy

def main():
    # TODO: Input da acquisire da file

    # Leggere file input
    in_file = open("input.txt", "r")
    text = in_file.readline()
    R = int(text[0])  # 3 rows
    C = int(text[1])  # 5 columns
    L = int(text[2])  # min 1 of each ingredient per slice
    H = int(text[3])  # max 6 cells per slice

    index = 3
    A = np.ones((3,2))
    for column in range(C):
        for row in range(R):
            A[row, column] = int(text[index])
            index = index + 1


    in_file.close()

    #A = [["T", "T", "T", "T", "T"],
    #    ["T", "M", "M", "M", "T"],
    #    ["T", "T", "T", "T", "T"]]

    # Scrivere file output
    out_file = open("output.txt", "w")
    x = 52
    out_file.write(str(x))
    out_file.close()

if __name__ == '__main__':
    main()