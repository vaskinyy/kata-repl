from repl.interpreter import Interpreter


def main():
    # simple REPL
    interpreter = Interpreter()
    while True:
        try:
            line = input('> ')
            res = interpreter.run(line)
            print(res)
        except KeyboardInterrupt:
            print("")
            print("Bye")
            break


if __name__ == '__main__':
    main()
