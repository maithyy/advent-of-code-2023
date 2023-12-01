def main():
    result = 0
    with open('input.txt') as f:
        for line in f:
            line = list(filter(lambda x: x.isdigit(), line))
            value = int(line[0] + line[-1])
            result += value
    return result


if __name__ == "__main__":
    print(main())

# Cleaner version
#
# def getFirstValue(line):
#     for i in range(len(line)):
#         if line[i].isdigit():
#             return str(line[i])
            
# def getLastValue(line):
#     for i in range(len(line)-1, -1, -1):
#         if line[i].isdigit():
#             return str(line[i])

# def main():
#     result = 0
#     with open('input.txt') as f:
#         for line in f:
#             firstValue = getFirstValue(line)
#             lastValue = getLastValue(line)
#             result += int(firstValue + lastValue)
#     return result
