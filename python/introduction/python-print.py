from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    value = 1
    divided = 10
    for x in range(2, n + 1):
        if x % divided == 0:
            divided = divided * 10
        value = value * divided + x
    if n >= 1:
        print(value)
