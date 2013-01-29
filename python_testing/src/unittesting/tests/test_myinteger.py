import myinteger
import unittest2


class TestMyInteger(unittest2.TestCase):

    def setUp(self):
        self.i = myinteger.MyInteger(4)

    def test_add_simple(self):
        """Make sure single digit addition works"""
        self.assertEqual(self.i.add(2), 6)

    def test_divide(self):
        """Make sure single digit division works"""
        self.assertEqual(self.i.divide(2), 2)

    def test_multiply(self):
        """Make sure single digit multiplication works"""
        self.assertEqual(self.i.multiply(2), 8)

    def test_subtract(self):
        """Make sure single digit subtraction works"""
        self.assertEqual(self.i.subtract(2), 2)

if __name__ == '__main__':
    unittest2.main()
