cdef fun3():
    try:
        return 5
    finally:
        print("test")
        return 10

cpdef fun4():
    return fun3()
