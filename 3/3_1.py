def main():
    gamma = ''
    epsilon = ''
    file = open('input.txt')

    listOfLines = list(file)

    index = 0
    while index < 12:
        countOfOnes = 0
        for line in listOfLines:
            if line.strip()[index] == '1':
                countOfOnes += 1
        if countOfOnes > len(listOfLines) / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
        index += 1

    print(gamma)
    print(epsilon)
    print(int(gamma, 2))
    print(int(epsilon, 2))

    print(int(gamma, 2) * int(epsilon, 2))


if __name__ == '__main__':
    main()
