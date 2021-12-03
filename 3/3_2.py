def main():

    file = open('input.txt')

    listOfLines = list(file)

    index = 0
    while index < 12:
        countOfOnes = 0
        listWithOnes = []
        listWithZeros = []
        for line in listOfLines:
            if line.strip()[index] == '1':
                countOfOnes += 1
                listWithOnes.append(line.strip())
            else:
                listWithZeros.append(line.strip())

        if countOfOnes >= len(listOfLines) / 2:
            listOfLines = listWithOnes
        else:
            listOfLines = listWithZeros
        index += 1
        if (len(listOfLines) == 1):
            break

    num1 = int(listOfLines[0], 2)

    file2 = open('input.txt')
    listOfLines2 = list(file2)

    index = 0

    while index < 12:
        countOfOnes = 0
        listWithOnes = []
        listWithZeros = []
        for line in listOfLines2:
            if line.strip()[index] == '1':
                countOfOnes += 1
                listWithOnes.append(line.strip())
            else:
                listWithZeros.append(line.strip())

        if countOfOnes < len(listOfLines2) / 2:
            listOfLines2 = listWithOnes
        else:
            listOfLines2 = listWithZeros
        print(listOfLines2)
        index += 1
        if (len(listOfLines2) == 1):
            break

    num2 = int(listOfLines2[0], 2)

    print(num1)
    print(num2)

    print(num1 * num2)


if __name__ == '__main__':
    main()
