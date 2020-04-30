cdef fun1():
    try:
        return 5
    finally:
        return 10

cpdef fun2():
    return fun1()
