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
        with self.assertRaises(Exception) as context:
            res = interpreter.input("fn add x y => x + z")

    def test_function_add_call(self):
        interpreter = Interpreter()
        res = interpreter.input("fn add x y => x + y")
        self.assertEqual(res, "")

        res1 = interpreter.input("add 1 2")
        self.assertEqual(3.0, res1)

    def test_function_echo_call(self):
        interpreter = Interpreter()
        res = interpreter.input("fn echo a => a")
        self.assertEqual(res, "")

        res1 = interpreter.input("echo 2")
        self.assertEqual(2.0, res1)

    def test_task_1(self):
        interpreter = Interpreter()
        res = interpreter.input("x = 7")
        self.assertEqual(7.0, res)

        res1 = interpreter.input("x")
        self.assertEqual(7.0, res1)

    def test_task_2(self):
        interpreter = Interpreter()
        res = interpreter.input("x = 7")
        self.assertEqual(7.0, res)

        res1 = interpreter.input("x + 6")
        self.assertEqual(13.0, res1)

    def test_task_3(self):
        interpreter = Interpreter()
        with self.assertRaises(Exception) as context:
            res = interpreter.input("y + 3")

    def test_task_4(self):
        interpreter = Interpreter()
        res = interpreter.input("x = 13 + (y = 3)")
        self.assertEqual(16.0, res)

        res1 = interpreter.input("x")
        self.assertEqual(16.0, res1)

        res2 = interpreter.input("y")
        self.assertEqual(3.0, res2)

    def test_task_5(self):
        interpreter = Interpreter()
        with self.assertRaises(Exception) as context:
            res = interpreter.input("fn avg => (x + y) / 2")

    def test_task_6(self):
        interpreter = Interpreter()
        res = interpreter.input("fn avg x y => (x + y) / 2")
        self.assertEqual("", res)

        res1 = interpreter.input("a = 2")
        self.assertEqual(2.0, res1)

        res2 = interpreter.input("b = 4")
        self.assertEqual(4.0, res2)

        res3 = interpreter.input("avg a b")
        self.assertEqual(3.0, res3)

    def test_task_7(self):
        interpreter = Interpreter()
        with self.assertRaises(Exception) as context:
            res = interpreter.input("fn add x y => x + z")

    def test_task_8(self):
        interpreter = Interpreter()
        res = interpreter.input("fn echo x => x")
        self.assertEqual("", res)

        res1 = interpreter.input("fn add x y => x + y")
        self.assertEqual("", res1)

        res2 = interpreter.input("add echo 4 echo 3")
        self.assertEqual(7.0, res2)

    def test_task_9(self):
        interpreter = Interpreter()
        res = interpreter.input("fn inc x => x + 1")
        self.assertEqual("", res)

        res1 = interpreter.input("a = 0")
        self.assertEqual(0.0, res1)

        res2 = interpreter.input("a = inc a")
        self.assertEqual(1.0, res2)

        res3 = interpreter.input("fn inc x => x + 2")
        self.assertEqual("", res3)

        res4 = interpreter.input("a = inc a")
        self.assertEqual(3.0, res4)

    def test_task_10(self):
        interpreter = Interpreter()
        with self.assertRaises(Exception) as context:
            res = interpreter.input("fn add x x => x + x")

    def test_task_11(self):
        interpreter = Interpreter()
        with self.assertRaises(Exception) as context:
            res = interpreter.input("(fn echo x => x)")

    def test_task_12(self):
        interpreter = Interpreter()
        res = interpreter.input("fn avg one two => (one + two) / 2")
        self.assertEqual("", res)

        res1 = interpreter.input("one = 2")
        self.assertEqual(2.0, res1)

        res2 = interpreter.input("b = 4")
        self.assertEqual(4.0, res2)

        res3 = interpreter.input("avg one b")
        self.assertEqual(3.0, res3)

    def test_task_13(self):
        interpreter = Interpreter()
        res = interpreter.input("fn one => 2")
        self.assertEqual("", res)

        res1 = interpreter.input("one")
        self.assertEqual(2.0, res1)

    def test_task_43(self):
        interpreter = Interpreter()

        res1 = interpreter.input("2 / 2 + 3 * 4 - 6")
        self.assertEqual(7.0, res1)


