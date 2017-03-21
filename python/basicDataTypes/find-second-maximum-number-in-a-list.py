if __name__ == '__main__':
    n = int(raw_input())
    ol = sorted(map(int, raw_input().split()), reverse=True)
    for n in xrange(1, len(ol)):
        if ol[n] < ol[0]:
            print ol[n]
            break
