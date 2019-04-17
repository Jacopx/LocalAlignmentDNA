import sys


def main(a, b, match, miss, gap):
    # Creating the matrix
    m = []
    for i in range(len(a) + 1):
        r = []
        for j in range(len(b) + 1):
            r.append(0)
        m.append(r)

    for i in range(1, len(m)):
        for j in range(1, len(m[i])):
            # Check if match or not
            if a[i - 1] == b[j - 1]:
                topleft = m[i - 1][j - 1] + match
            else:
                topleft = m[i - 1][j - 1] + miss

            # Compute other two values
            top = m[i - 1][j] + gap
            left = m[i][j - 1] + gap

            # Compute the max
            m[i][j] = max(topleft, top, left, 0)

    print("a:%s" % a)
    print("b:%s" % b)

    # Initialing variable for traceback
    af = []
    align = []
    bf = []
    global_value = 0
    first_time = True

    for i in range(len(m) - 1):
        if a[len(a) - i - 1] == b[len(b) - i - 1]:
            if first_time:
                global_value = m[len(b) - i][len(a) - i]
                first_time = False
            af.append(a[len(a) - i - 1])
            align.append("|")
            bf.append(b[len(b) - i - 1])

    print("Global alignment score: %f\n" % global_value)

    print_matrix(m)

    print("\nFinal alignment:")
    print_list(af)
    print_list(align)
    print_list(bf)


def print_list(l):
    for i in range(len(l), 0, -1):
        print(l[i - 1], end='')
    print()


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end='\t')
        print()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))