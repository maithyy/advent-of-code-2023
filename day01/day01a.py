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
