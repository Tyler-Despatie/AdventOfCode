
def main():
    count = 0
    with open("input.txt") as f:
        for line in f:
            for n, c in enumerate(line):
                if (c == '('):
                    count = count + 1
                if (c == ')'):
                    count = count - 1
                if (count == -1):
                    print("hit -1 at {}".format((n + 1)))
    print(count)
if __name__ == '__main__':
    main()
