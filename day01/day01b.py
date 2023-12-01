def getFirstValue(line, numbers):
    for i in range(len(line)):
        if line[i].isdigit():
            return str(line[i])
        for number in numbers:
            if line[i:].startswith(number):
                return str(numbers[number])
            
def getLastValue(line, numbers):
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            return str(line[i])
        for number in numbers:
            if line[i:].startswith(number):
                return str(numbers[number])

def main():
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight" : 8, "nine": 9}
    result = 0
    with open('example.txt') as f:
        for line in f:
            firstValue = getFirstValue(line, numbers)
            lastValue = getLastValue(line, numbers)
            result += int(firstValue + lastValue)


    return result


if __name__ == "__main__":
    print(main())
