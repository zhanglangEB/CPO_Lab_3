from multi_dispatch import multimethod


@multimethod(int, int)
def foo(a, b):
    return a + b


@multimethod(float, int)
def foo(a, b):
    return a + b


@multimethod(float, float)
def foo(a, b):
    return a + b


@multimethod(int, float)
def foo(a, b):
    return a + b


@multimethod(str, str)
def foo(a, b):
    return a + b


@multimethod(str, int)
def foo(a, b):
    return a + str(b)


@multimethod(int, str)
def foo(a, b):
    return str(a) + b


@multimethod(str, float)
def foo(a, b):
    return a + str(b)


@multimethod(float, str)
def foo(a, b):
    return str(a) + b


@multimethod(list, int)
def foo(a, b):
    a.append(b)
    return a


@multimethod(int, list)
def foo(a, b):
    b.append(a)
    return b


@multimethod(list, list)
def foo(a, b):
    a.extend(b)
    return a


@multimethod(int, int)
@multimethod(int)
def foo(a, b=1):
    return a + b


@multimethod(float, float)
@multimethod(float)
def foo(a, b=1.0):
    return a + b


@multimethod(str, str)
@multimethod(str)
def foo(a, b='hello '):
    return b + a


@multimethod(list, int, int)
@multimethod(list, int)
@multimethod(list)
def foo(a, b=1, c=1):
    a.append(b)
    a.append(c)
    return a


class A(object):
    def __init__(self):
        print("This is a A")


class B(A):
    def __init__(self):
        print("This is a B")


class C(B):
    def __init__(self):
        print("This is a C")


class D(object):
    def __init__(self):
        print("This is a D")


class E(D):
    def __init__(self):
        print("This is a E")


class F(E):
    def __init__(self):
        print("This is a F")


class G(A, D):
    def __init__(self):
        print("This is a G")


@multimethod(A, A)
def foo(a, b):
    print(type(a), type(b))
    return 'AA'


@multimethod(D, D)
def foo(a, b):
    print(type(a), type(b))
    return 'DD'


@multimethod(A, D)
def foo(a, b):
    print(type(a), type(b))
    return 'AD'


@multimethod(D, A)
def foo(a, b):
    print(type(a), type(b))
    return 'DA'


