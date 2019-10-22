"""Demonstrates tuples
"""


def demonstrate_tuples():
    """Creating and using tuples.
    """

    # Create and print 1-tuple, 2-tuple, mixed-type n-tuple
    w = ('Woodstock', )
    w = 'Woodstock',
    print(w)
    print(type(w))
    # w = 'Woodstock', 1969
    w = 'Woodstock', 1969, True
    print(w)
    print()

    # Access elements of a tuple using []
    print(w[1])
    print()

    # Demonstrate that tuples are immutable
    # w[1] = 1967                                     # No way, tuples are immutable!
    # 'Woodstock'[1] = 'u'                            # No way, strings are immutable!


def demonstrate_zip():
    """Using the built-in zip() function with tuples and double-counter for-loop.
    """

    w = 'Woodstock', 1969, 'Bethel'
    m = 'Monterey Pop', 1967, 'Monterey'
    z = zip(w, m)
    print(z)
    print(list(z))
    for i, j in z:                                  # zip() returns an iterator, which can be exhausted only once
        print(str(i) + ',', str(j))                 # (so, this print is "empty" because of the previous print)


def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    w = 'Woodstock', 1969, 'Bethel'
    name, year, place = w
    print(name, year, place)
    print((name, year, place))
    print()


if __name__ == '__main__':

    # pass
    # demonstrate_tuples()
    # demonstrate_zip()
    demonstrate_packing()
