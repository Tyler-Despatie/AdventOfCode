import sys
import re

def main():
    lights = [
        [0 for y in range(1000)]
        for x in range(1000)
    ]
    with open("input.txt") as f:
        for line in f:
            mode, x1, y1, x2, y2 = re.match('(.*) (\d+),(\d+) through (\d+),(\d+)', line.strip()).groups()
            x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))

            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if mode == 'turn on':
                        lights[x][y] += 1
                    elif mode == 'turn off':
                        if lights[x][y] > 0:
                            lights[x][y] -= 1
                    else:
                        lights[x][y] += 2

    print(sum(
        lights[x][y]
        for x in range(1000)
        for y in range(1000)
    ))

if __name__ == '__main__':
    main()