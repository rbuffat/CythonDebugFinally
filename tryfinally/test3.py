def fun5():
    try:
        return 5
    finally:
        return 10


def fun6():
    return fun5()
