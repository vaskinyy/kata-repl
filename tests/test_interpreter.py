import unittest

from repl.interpreter import Interpreter


class Test_Interpreter(unittest.TestCase):
    def test_empty(self):
        interpreter = Interpreter()
        res = interpreter.input("")
        self.assertEqual("", res)

    def test_invalid_input(self):
        interpreter = Interpreter()
        with self.assertRaises(Exception) as context:
            res = interpreter.input("1 2")

    def test_adding(self):
        interpreter = Interpreter()
        res = interpreter.input("1 + 7")
        self.assertEqual(res, 8.0)

    def test_multiply(self):
        interpreter = Interpreter()
        res = interpreter.input("1 + 7 * 5")
        self.assertEqual(res, 36.0)

    def test_multiply_2(self):
        interpreter = Interpreter()
        res = interpreter.input("7 * 5 + 1")
        self.assertEqual(res, 36.0)

    def test_brackets(self):
        interpreter = Interpreter()
        res = interpreter.input("7 * (5 + 1)")
        self.assertEqual(res, 42.0)

    def test_brackets_2(self):
        interpreter = Interpreter()
        res = interpreter.input("((7 * 5) + 1)")
        self.assertEqual(res, 36.0)

    def test_add_mul_div(self):
        interpreter = Interpreter()
        res = interpreter.input("1+2*3+4/2")
        self.assertEqual(res, 9.0)

    def test_per_cent(self):
        interpreter = Interpreter()
        res = interpreter.input("1+3%2")
        self.assertEqual(res, 2.0)

    def test_assignment(self):
        interpreter = Interpreter()
        res = interpreter.input("x = 4")
        self.assertEqual(res, 4.0)
        res1 = interpreter.input("x")
        self.assertEqual(res1, 4.0)

    def test_assignment_complex(self):
        interpreter = Interpreter()
        res = interpreter.input("x = y = 4")
        self.assertEqual(res, 4.0)
        res1 = interpreter.input("x")
        self.assertEqual(res1, 4.0)
        res2 = interpreter.input("y")
        self.assertEqual(res2, 4.0)

    def test_assignemnt_plus(self):
        interpreter = Interpreter()
        res = interpreter.input("x = 5+4")
        self.assertEqual(res, 9.0)
        res1 = interpreter.input("x * 10")
        self.assertEqual(res1, 90.0)

    def test_arithmetics(self):
        data = [
            ['1+1', 2],
            ['1 - 1', 0],
            ['1* 1', 1],
            ['1 /1', 1],
            ['-123', -123],
            ['123', 123],
            ['2 /2+3 * 4.75- -6', 21.25],
            ['12* 123', 1476],
            ['2 / (2 + 3) * 4.33 - -6', 7.732],
        ]
        interpreter = Interpreter()

        for d in data:
            res = interpreter.input(d[0])
            self.assertEqual(res, d[1])

    def test_function_definitions(self):
        interpreter = Interpreter()
        res = interpreter.input("fn add x y => x + z")
        self.assertEqual(res, "")