import hashlib


def main():
    for i in range(0, 1000000000):
        phrase = "iwrupvqb" + str(i)
        m = hashlib.md5(phrase.encode("utf-8"))
        first_five = str(m.hexdigest())[:6]
        if first_five == "000000":
            print(phrase + " " + m.hexdigest())
            break

if __name__ == '__main__':
    main()
