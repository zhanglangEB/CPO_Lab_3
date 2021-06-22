import unittest
from methods import *


class TestMethods(unittest.TestCase):

    def test_positional(self):
        self.assertEqual(foo(1, 2), 3)
        self.assertEqual(foo(1.0, 2.0), 3.0)
        self.assertEqual(foo(1.0, 2), 3.0)
        self.assertEqual(foo(1, 2.0), 3.0)
        self.assertEqual(foo('hello ', 'world!'), 'hello world!')
        self.assertEqual(foo('num=', 2), 'num=2')
        self.assertEqual(foo(2, ' apples'), '2 apples')
        self.assertEqual(foo('num=', 2.0), 'num=2.0')
        self.assertEqual(foo(2.0, ' apples'), '2.0 apples')
        self.assertEqual(foo([1, 2], 3), [1, 2, 3])
        self.assertEqual(foo(3, [1, 2]), [1, 2, 3])
        self.assertEqual(foo([1, 2], [3, 4]), [1, 2, 3, 4])

    def test_optional(self):
        self.assertEqual(foo(1), 2)
        self.assertEqual(foo(1.0), 2.0)
        self.assertEqual(foo('world!'), 'hello world!')
        self.assertEqual(foo([]), [1, 1])

    def test_named(self):
        self.assertEqual(foo(a=1, b=1), 2)
        self.assertEqual(foo(1, b=1), 2)
        self.assertEqual(foo(a=1.0, b=1.0), 2.0)
        self.assertEqual(foo(1, b=1.0), 2.0)
        self.assertEqual(foo(a='hello ', b='world!'), 'hello world!')
        self.assertEqual(foo(a=2, b='apples'), '2apples')
        self.assertEqual(foo(a=2.0, b='apples'), '2.0apples')
        self.assertEqual(foo(a='num=', b=1), 'num=1')
        self.assertEqual(foo(a='num=', b=1.0), 'num=1.0')

    def test_inherit(self):
        self.assertEqual(foo(A(), A()), 'AA')
        self.assertEqual(foo(B(), B()), 'AA')
        self.assertEqual(foo(B(), C()), 'AA')
        self.assertEqual(foo(C(), C()), 'AA')

        self.assertEqual(foo(D(), D()), 'DD')
        self.assertEqual(foo(E(), E()), 'DD')
        self.assertEqual(foo(E(), F()), 'DD')
        self.assertEqual(foo(F(), F()), 'DD')

        self.assertEqual(foo(A(), D()), 'AD')
        self.assertEqual(foo(B(), E()), 'AD')
        self.assertEqual(foo(C(), F()), 'AD')

        self.assertEqual(foo(D(), A()), 'DA')
        self.assertEqual(foo(E(), B()), 'DA')
        self.assertEqual(foo(F(), C()), 'DA')

        self.assertEqual(foo(E(), E()) in ['AA', 'DD', 'AD', 'DA'], True)

