def main():
    file = open('test_input.txt')
    lanternFish = []
    result = 0

    timer = 6

    lanternFish = file.read()
    lanternFish = lanternFish.split(',')
    lanternFish = list(map(str.strip, lanternFish))
    lanternFish = list(map(int, lanternFish))

    print(lanternFish)

    index = 0
    for i in range(1, 19):
        newFish = 0
        index = 0
        while index < len(lanternFish):
            lanternFish[index] -= 1
            if lanternFish[index] == -1:
                newFish += 1
                lanternFish[index] = 6
            index += 1
        for x in range(newFish):
            lanternFish.append(8)

        result += 1
        print(f'After {i} days: {len(lanternFish)}')


if __name__ == '__main__':
    main()
