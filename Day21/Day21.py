import argparse
import os.path

from typing import Dict
from typing import FrozenSet
from typing import NamedTuple
from typing import Set


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

class Recipe(NamedTuple):
    ingredients: FrozenSet[str]
    allergens: FrozenSet[str]


def part1(s: str) -> int:
    recipes = []

    for line in s.strip().splitlines():
        begin, _, rest = line.partition('(contains ')

        begin = begin.strip()
        ingredients = frozenset(begin.split())

        rest = rest.strip(')')
        allergens = frozenset(rest.split(', '))
        recipes.append(Recipe(ingredients, allergens))

    print(recipes)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        part1(f.read())

    return 0

if __name__ == '__main__':
    exit(main())