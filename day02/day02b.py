def get_fewest(cube_sets):
    result_dict = {}
    for s in cube_sets:
        s = s.split(",")
        for pair in s:
            amt, color = pair.split()
            amt = int(amt)
            if color in result_dict:
                result_dict[color] = max(result_dict[color], amt)
            else:
                result_dict[color] = amt
    return result_dict


def main():
    result = 0
    with open('input.txt') as f:
        for line in f:
            _, cube_sets = line.strip().split(': ')
            cube_sets = cube_sets.split('; ')
            power = 1
            for val in get_fewest(cube_sets).values():
                power *= val
            result += power
        
    return result

if __name__ == "__main__":
    print(main())
