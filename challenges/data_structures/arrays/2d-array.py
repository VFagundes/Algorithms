# https://www.hackerrank.com/challenges/2d-array/problem
import sys, os
import operator

table = []

table = [
    [2, 4, 5, 6, 727, 453],
    [21, 24, 335, 6, 77, 43],
    [29, 448, 275, 36, 717, 6543],
    [25, 14, 59, 61, 7327, 435],
    [23, 141, 95, 161, 7217, 643],
    [21, 42, 556, 62, 757, 423],
    [12, 445, 53, 16, 717, 143]]


def is_valid_HG(tb, row_index, col_index):
    VALID_COLUMN_LENGTH = 3
    VALID_ROW_LENGTH = 3
    is_valid = True
    row_length = len(tb[row_index:])  # index that i am
    # validate columns size
    is_valid &= row_length >= VALID_ROW_LENGTH
    if is_valid:
        column_length = len(tb[row_index][col_index:])
        is_valid &= column_length >= VALID_COLUMN_LENGTH
    return is_valid


def iterate_table(table):
    length = len(table)
    j = i = 0
    hour_glasses = []
    while i < length:
        row = table[i]
        while j < len(row):
            if is_valid_HG(table, i, j):
                hour_glasses.append(row[j:j + 3])
                last_index = len(hour_glasses) - 1
                hour_glasses[last_index].append(table[i + 1][j + 1])
                hour_glasses[last_index].extend(table[i + 2][j:j + 3])
            else:
                break
            j += 1
        i += 1
        j = 0
    return hour_glasses


hgs = iterate_table(table)
sums = map(lambda x: reduce(operator.add, x), hgs)
sums.sort(reverse=True)
print sums[0]
