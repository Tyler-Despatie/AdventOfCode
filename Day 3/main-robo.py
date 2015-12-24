from collections import Counter

def main():
    with open("input.txt") as f:
        for line in f:
            line = line.strip()

            x, y, xR, yR = 0, 0, 0, 0
            pathSanta = [(x, y)]
            pathRobo = [(xR, yR)]

            duplicates = 0
            houses = 1

            santapath = 0
            pathRobo.pop()

            for c in line:
                if (santapath == 0):
                    if c == '^':
                        y += 1
                    elif c == '>':
                        x += 1
                    elif c == '<':
                        x -= 1
                    elif c == 'v':
                        y -= 1

                    pathSanta.append((x, y))
                    santapath = 1
                else:
                    if c == '^':
                        yR += 1
                    elif c == '>':
                        xR += 1
                    elif c == '<':
                        xR -= 1
                    elif c == 'v':
                        yR -= 1
                    pathRobo.append((xR, yR))
                    santapath = 0
                houses += 1

            for coord in pathRobo:
                pathSanta.append(coord)

            #print(pathSanta)            
            for k, v in Counter(pathSanta).most_common():
                 if (v > 1):
                     duplicates += (v-1)
            print(line + " " + str(houses) + " homes duplicates= " + str(duplicates)) 
            print("Homes atleast once : " + str(houses-duplicates))

if __name__ == '__main__':
    main()