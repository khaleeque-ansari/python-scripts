"""
Python has recursion limit of 997. You can change the recursion limit with sys.setrecursionlimit
"""


def dream(x):
    print("Dreaming", x)
    dream(x + 1)


if __name__ == '__main__':
    dream(1)
