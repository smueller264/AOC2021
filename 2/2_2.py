def main():
    horizontal = 0
    depth = 0
    aim = 0

    file = open('input.txt')
    for line in file:
        operator = line.split()[0]
        operand = int(line.split()[1])
        if (operator == "forward"):
            horizontal += operand
            depth += aim * operand
        elif (operator == 'down'):
            aim += operand
        elif (operator == 'up'):
            aim -= operand
    print(horizontal)
    print(depth)
    print(horizontal * depth)


if __name__ == '__main__':
    main()
