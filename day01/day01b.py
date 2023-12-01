numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight" : 8, "nine": 9}

def getFirstValue(line):
    for i in range(len(line)):
        if line[i].isdigit():
            return str(line[i])
        for number in numbers:
            if line[i:].startswith(number):
                return str(numbers[number])
            
def getLastValue(line):
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            return str(line[i])
        for number in numbers:
            if line[i:].startswith(number):
                return str(numbers[number])

def main():
    result = 0
    with open('input.txt') as f:
        for line in f:
            firstValue = getFirstValue(line)
            lastValue = getLastValue(line)
            result += int(firstValue + lastValue)


    return result


if __name__ == "__main__":
    print(main())
