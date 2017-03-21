if __name__ == '__main__':
    N = int(raw_input())
    the_list = []
    for x in xrange(N):
        inst = raw_input().lower().strip().split(" ")

        if inst[0] == "insert":
            the_list.insert(int(inst[1]), int(inst[2]))
        elif inst[0] == "print":
            print the_list
        elif inst[0] == "remove":
            the_list.remove(int(inst[1]))
        elif inst[0] == "append":
            the_list.append(int(inst[1]))
        elif inst[0] == "sort":
            the_list.sort()
        elif inst[0] == "pop":
            the_list.pop()
        elif inst[0] == "reverse":
            the_list.reverse()
