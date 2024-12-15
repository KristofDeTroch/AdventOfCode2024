def isSafe(report: list[int])->bool:
    down = True
    up = True
    for i in range(1, len(report)):
        prev = report[i-1]
        curr = report[i]
        distance = abs(prev-curr)
        if not (distance >=1 and distance <=3):
            return False
        if down:
            down = curr < prev
        if up:
            up = curr > prev
        if not (up or down):
            return False
    return up or down

def isSafeDampenendUp(report: list[int], removed:bool)->bool:

    for i in range(1, len(report)):
        prev = report[i-1]
        curr = report[i]
        distance = abs(prev-curr)

        if (not curr > prev) or not (distance >=1 and distance <=3):
            if not removed :
                newPrevList = report[:i-1] + report[i:]
                newCurrList = report[:i] + report[i+1:]
                return isSafeDampenendUp(newPrevList, True) or isSafeDampenendUp(newCurrList, True)
            
            return False
    return True
def isSafeDampenendDown(report: list[int], removed)->bool:
    for i in range(1, len(report)):
        prev = report[i-1]
        curr = report[i]
        distance = abs(prev-curr)
        if (not curr < prev) or (not (distance >=1 and distance <=3)):
            if not removed :
                newPrevList = report[:i-1] + report[i:]
                newCurrList = report[:i] + report[i+1:]
                return isSafeDampenendDown(newCurrList, True) or isSafeDampenendDown(newPrevList, True)
            return False
     
    return True


with open('day02/input.txt', 'r') as file:
    reports = []
    for line in file:
        levels = line.strip().split(" ")
        reports.append(list(map(lambda x: int(x), levels)))

    safeReports = filter(lambda r: isSafe(r), reports)
    print(len(list(safeReports)))
    safeDampenendReports = filter(lambda r: isSafeDampenendUp(r, False) or isSafeDampenendDown(r, False), reports)
    print(len(list(safeDampenendReports)))