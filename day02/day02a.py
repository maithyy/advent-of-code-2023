possible = {"red": 12, "green": 13, "blue": 14}
def possible_game(cube_sets):
    for s in cube_sets:
        s = s.split(",")
        for pair in s:
            amt, color = pair.split()
            amt = int(amt)
            if color in possible and possible[color] < amt:
                return False
    return True

def main():
    result = 0
    with open('input.txt') as f:
        for line in f:
            game_id, cube_sets = line.strip().split(': ')
            game_id = int(game_id.split()[1])
            cube_sets = cube_sets.split('; ')
            if possible_game(cube_sets):
                result += game_id
        
    return result

if __name__ == "__main__":
    print(main())
