if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

    print [[col, row, depth] for col in xrange(x + 1) for row in xrange(y + 1) for depth in xrange(z + 1) if col + row + depth != n]
