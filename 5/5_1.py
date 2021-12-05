def main():

    vectors = []
    file = open("input.txt")
    for line in file:
        vector = []
        line = line.split('->')
        line = list(map(str.strip, line))

        for item in line:
            temp = []
            item = item.split(',')
            for num in item:
                temp.append(int(num))
            vector.append(temp)

        if (vector[0][0] == vector[1][0]) or (vector[0][1] == vector[1][1]):
            vectors.append(vector)

    for v in vectors:
        print(v)

    grid = [[0]*999 for k in range(999)]

    for c in grid:
        print(c)

    for vec in vectors:
        print(f'vector: {vec}')
        x1 = vec[0][0]
        y1 = vec[0][1]
        x2 = vec[1][0]
        y2 = vec[1][1]
        xdelta = abs(vec[0][0] - vec[1][0])
        ydelta = abs(vec[0][1] - vec[1][1])
        print(f'xdelta: {xdelta} ydelta: {ydelta}')
        if xdelta != 0:
            if x1 > x2:
                start = x2
                end = x1
            else:
                start = x1
                end = x2
            print(f'start: {start}')
            for x in range(start, end+1):
                print(f' xpoint:  {x} {y1}')
                grid[y1][x] += 1

        if ydelta != 0:
            if y1 > y2:
                start = y2
                end = y1
            else:
                start = y1
                end = y2
            print(f'start: {start}')
            for y in range(start, end+1):
                print(f' ypoint:  {x1} {y}')
                grid[y][x1] += 1
        print()
    result = 0
    for pr in grid:
        for num in pr:
            if num >= 2:
                result += 1
        print(pr)

    print(f'result {result}')


if __name__ == '__main__':
    main()


# x1, y1 - x2, y2

# x1 = x2
# y1 = y2

# v[0] = y[0]
