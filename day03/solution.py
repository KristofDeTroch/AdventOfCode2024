
enabled = True

def multiply(input:str)-> int:
    result = 0
    cursor = 0
    while cursor < len(input):
        start = input.find("mul(", cursor)
        end = input.find(")", start)
        if end == -1 or start == -1:
            break
        numbers = input[start+4:end].split(',')
        if len(numbers) == 2:
            try:
                first = int(numbers[0])
                second = int(numbers[1])
                result += first *second
            except:
                pass
        cursor = start + 1
    return result

with open('day03/input.txt', 'r') as file:
    input = ""
    for line in file:
        input += line.strip()
    result = multiply(input)

    print(result)
    intermediary = input.split("don't()")
    secondResult = multiply(intermediary[0])
    for i in range(1, len(intermediary)):
        nextIndex = intermediary[i].find('do()')
        secondResult += multiply(intermediary[i][nextIndex:])
    print(secondResult)

