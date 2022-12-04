from typing import Dict



def get_letters_worth() -> Dict[str, int]:
    return {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

def get_points_for_result() -> Dict[str, int]:
    return {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

def get_game_results_part_1() -> Dict[str, int]:
    return {
        "A X\n": 3,
        "A Y\n": 6,
        "A Z\n": 0,
        "B X\n": 0,
        "B Y\n": 3,
        "B Z\n": 6,
        "C X\n": 6,
        "C Y\n": 0,
        "C Z\n": 3,
    }

def get_game_results() -> Dict[str, int]:
    return {
        "A X\n": 3,
        "A Y\n": 4,
        "A Z\n": 8,
        "B X\n": 1,
        "B Y\n": 5,
        "B Z\n": 9,
        "C X\n": 2,
        "C Y\n": 6,
        "C Z\n": 7,
    }

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    letters_worth = get_letters_worth()
    game_results = get_game_results()

    def find_score(line: str) -> int:
        score = 0
        opponent, player = line.split()
        # score += letters_worth[player]
        score += game_results[line]
        return score


    def find_total_score() -> int:
        return sum(
            find_score(line) for line in lines
        )

    result = find_total_score()
    print(result)

if __name__ == "__main__":
    main()