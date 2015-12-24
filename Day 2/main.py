
def main():
    totalSum = 0
    totalPerim = 0
    with open("input.txt") as f:
        for n, line in enumerate(f):
            dimensions = line.strip().split('x')
            length = int(dimensions[0])
            width = int(dimensions[1])
            height = int(dimensions[2])

            sides = [(length*width), (width*height), (height*length)]
            sidesPerim = sorted([length, width, height])

            shortest = ((sidesPerim[0]+sidesPerim[0]) + (sidesPerim[1]+sidesPerim[1]))
            print(shortest)
            eachside = (length*width*height)
            totalPerim += (eachside + shortest)
            smallestSide = min(sides)
            sumOfEq = 0
            for side in sides:
                sumOfEq += (side * 2)


            _totalSum = (smallestSide + sumOfEq)
            totalSum = (totalSum + _totalSum)
            # print("{} x {} x {} = {} + {} = {}".format(length,
            #                                            width,
            #                                            height,
            #                                            sumOfEq,
            #                                            smallestSide,
            #                                            _totalSum))
    print(totalSum)
    print(totalPerim)
if __name__ == '__main__':
    main()
