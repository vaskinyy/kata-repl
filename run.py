
def main():
    # simple REPL
    while True:
        try:
            res = input('> ')
            print(res)
        except KeyboardInterrupt as ex:
            print("")
            print("Bye")
            break


if __name__ == '__main__':
    main()
