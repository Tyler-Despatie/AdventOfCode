from collections import Counter
def main():
    
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            x, y = 0, 0
            path = [(x, y)]
            duplicates = 0
            houses = 1
            for c in line:
                if c == '^':
                    y += 1
                elif c == '>':
                    x += 1
                elif c == '<':
                    x -= 1
                elif c == 'v':
                    y -= 1
                path.append((x, y))
                houses += 1
            #print(path)
            for k, v in Counter(path).most_common():
                if (v > 1):
                    duplicates += (v-1)
            print(line + " " + str(houses) + " homes duplicates= " + str(duplicates))
            print("Homes atleast once : " + str(houses-duplicates))
if __name__ == '__main__':
    main()
