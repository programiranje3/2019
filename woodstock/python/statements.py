"""Demonstrates peculiarities of if, for, while and other statements
"""


def demonstrate_branching():
    """Details and peculiarities of if statements.
    """

    # is compares id()'s, == compares contents
    w1 = 'Woodstock'
    w2 = 'Woodstock'
    if w1 == w2:
        print('w1 == w2')
    else:
        print('w1 != w2')
    if w1 is w2:
        print('w1 is w2')
    else:
        print('w1 is not w2')
    print()

    # id()'s are the same for equal strings, but not for lists, user class instances,...
    l1 = ['Woodstock']
    l2 = ['Woodstock']
    if l1 == l2:
        print('l1 == l2')
    else:
        print('l1 != l2')
    if l1 is l2:
        print('l1 is l2')
    else:
        print('l1 is not l2')
    print()

    # The condition of an if-statement need not necessarily be a boolean
    if l1:
        print(l1)
    else:
        print(False)
    print()

    # There can be more than one elif after if (no switch statement, use multiple elif instead)
    if not l1:
        print('not', l1)
    elif not w1:
        print('not', w1)
    else:
        print(False)
    print()


def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    """

    # It is not necessary to iterate through all elements of an iterable
    w3 = 'Woodstock' * 3
    print(w3)
    for c in w3[0:9]:
        print(c, end='')
    print()

    # Step in range()
    for c in range(0, len(w3), 2):
        print(w3[c], end=' ')
    print()

    # Unimportant counter (_)
    # break and continue
    for _ in 'Woodstock':
        print('W', end=' ')
        # break
    print()

    # while loop
    i = 0
    w = 'Woodstock'
    while i < len(w):
        print(w[i], end='')
        i += 1
    print()


if __name__ == '__main__':

    # pass
    # demonstrate_branching()
    demonstrate_loops()
