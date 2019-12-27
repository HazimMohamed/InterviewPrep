from enum import Enum
import sys
from copy import deepcopy


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def solve(island_matrix, m_width, m_height):
    def at(pos, offset=None):
        if offset is None:
            return (pos[0], pos[1]), island_matrix[pos[1]][pos[0]]
        elif offset == Direction.UP:
            return (pos[0], pos[1] - 1), island_matrix[pos[1] - 1][pos[0]]
        elif offset == Direction.DOWN:
            return (pos[0], pos[1] + 1), island_matrix[pos[1] + 1][pos[0]]
        elif offset == Direction.LEFT:
            return (pos[0] - 1, pos[1]), island_matrix[pos[1]][pos[0] - 1]
        elif offset == Direction.RIGHT:
            return (pos[0] + 1, pos[1]), island_matrix[pos[1]][pos[0] + 1]

    def raise_level(pos, target, blacklist=None):
        if blacklist is None:
            blacklist = [pos]
        else:
            blacklist.append(pos)

        pos, val = at(pos)
        for direction in Direction:
            neighbor, neighbor_val = at(pos, direction)
            if neighbor not in blacklist and val >= neighbor_val:
                raise_level(neighbor, target, blacklist)
        island_matrix[pos[1]][pos[0]] = target

    def pours_out(pos, blacklist=None):
        if blacklist is None:
            blacklist = [pos]
        else:
            blacklist.append(pos)

        # If the position is the ocean, it pours out
        if pos[0] == 0 or pos[0] == m_width-1 or pos[1] == 0 or pos[1] == m_height-1:
            return True

        has_reached_ocean = False
        this_val = at(pos)[1]
        for direction in Direction:
            try:
                loc, val = at(pos, direction)
                if val <= this_val and loc not in blacklist:
                    has_reached_ocean = has_reached_ocean or pours_out(loc, blacklist)
            except IndexError:
                continue
        return has_reached_ocean

    original = deepcopy(island_matrix)

    for y in range(1, m_height-1):
        for x in range(1, m_width-1):
            while not pours_out((x, y)):
                raise_level((x, y), island_matrix[y][x] + 1)

    # print('Original:')
    # print(np.matrix(original))
    # print('Rained On:')
    # print(np.matrix(island_matrix))

    diff = 0
    for old_row, new_row in list(zip(original, island_matrix)):
        for old_elem, new_elem in list(zip(old_row, new_row)):
            diff += new_elem - old_elem

    return diff


num_test_cases = int(input())
for i in range(num_test_cases):
    width, height = list(map(lambda a: int(a), input().split(' ')))
    matrix = []
    for row in range(height):
        matrix.append(list(map(lambda a: int(a), input().split(' '))))
    print('Case #{}: {}'.format(i+1, solve(matrix, width, height)))
    print('Case #{} done'.format(i + 1), file=sys.stderr)
