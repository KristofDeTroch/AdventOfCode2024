with open('day01/input.txt', 'r') as file:
    # Read each line in the file
    leftList = []
    rightList = []
    for line in file:
        # Print each line
        [left, right] = line.strip().split("   ")
        leftList.append(int(left))
        rightList.append(int(right))
    leftList.sort()
    rightList.sort()

    count = 0   
    for index in range(len(rightList)):
        l = leftList[index]
        r = rightList[index]
        count += abs(l-r)


    print(count)
    secondCount = 0
    for i in range(len(leftList)):
        l = leftList[i]
        r = rightList.count(l)
        print(l, r , secondCount)
        secondCount += l * r
    print(secondCount)