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

        print(f'vector {vector}')
        x1 = vector[0][0]
        y1 = vector[0][1]
        x2 = vector[1][0]
        y2 = vector[1][1]
        xdelta = abs(vector[0][0] - vector[1][0])
        ydelta = abs(vector[0][1] - vector[1][1])
        print(
            f'xdelta: {xdelta} = {x1} - {x2} | ydelta: {ydelta} = {y1} - {y2}')

        if (vector[0][0] == vector[1][0]) or (vector[0][1] == vector[1][1]) or xdelta == ydelta:
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
        xdelta = vec[0][0] - vec[1][0]
        ydelta = vec[0][1] - vec[1][1]
        absxdelta = abs(vec[0][0] - vec[1][0])
        absydelta = abs(vec[0][1] - vec[1][1])
        print(f'xdelta: {xdelta} ydelta: {ydelta}')

        if (absxdelta == absydelta):
            if (xdelta <= 0 and ydelta <= 0) or (xdelta >= 0 and ydelta >= 0):
                print('equal')
                if (x1 < x2):
                    startx = x1
                    starty = y1
                else:
                    startx = x2
                    starty = y2
                for step in range(0, absxdelta + 1):
                    print(f'step:{step}')
                    print(
                        f'startx({startx}) + step = {startx + step} | starty({starty}) + step = {starty + step}')
                    grid[starty + step][startx + step] += 1
                continue
            else:
                print('unequal')
                if (x1 < x2):
                    startx = x1
                    starty = y1
                else:
                    startx = x2
                    starty = y2
                for step in range(0, absxdelta + 1):
                    print(f'step:{step}')
                    print(
                        f'startx({startx}) + step = {startx + step} | starty({starty}) - step = {starty - step}')
                    grid[starty - step][startx + step] += 1
                continue

        if absxdelta != 0:
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
            continue

        if absydelta != 0:
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
