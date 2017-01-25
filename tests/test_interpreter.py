import unittest

from repl.interpreter import Interpreter


class Test_Interpreter(unittest.TestCase):
    def test_adding(self):
        interpreter = Interpreter()
        res = interpreter.run("1 + 7")
        self.assertEqual(res, 8.0)

    def test_multiply(self):
        interpreter = Interpreter()
        res = interpreter.run("1 + 7 * 5")
        self.assertEqual(res, 36.0)

    def test_multiply_2(self):
        interpreter = Interpreter()
        res = interpreter.run("7 * 5 + 1")
        self.assertEqual(res, 36.0)

    def test_brackets(self):
        interpreter = Interpreter()
        res = interpreter.run("7 * (5 + 1)")
        self.assertEqual(res, 42.0)

    def test_brackets_2(self):
        interpreter = Interpreter()
        res = interpreter.run("((7 * 5) + 1)")
        self.assertEqual(res, 36.0)

    def test_add_mul_div(self):
        interpreter = Interpreter()
        res = interpreter.run("1+2*3+4/2")
        self.assertEqual(res, 9.0)

    def test_per_cent(self):
        interpreter = Interpreter()
        res = interpreter.run("1+3%2")
        self.assertEqual(res, 2.0)
