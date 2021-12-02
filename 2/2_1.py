def main():
    horizontal = 0
    depth = 0
    file = open('input.txt')
    for line in file:
        operator = line.split()[0]
        if (operator == "forward"):
            horizontal += int(line.split()[1])
        elif (operator == 'down'):
            depth += int(line.split()[1])
        elif (operator == 'up'):
            depth -= int(line.split()[1])
    print(horizontal)
    print(depth)
    print(horizontal * depth)


if __name__ == '__main__':
    main()
