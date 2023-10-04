# -*- coding: utf-8 -*-
"""
Created on Thu May 11 20:48:30 2023

@author: Lenovo
"""

import random

grid = [['.']*4 for _ in range(5)]


def create_grid(rows, cols):
    grid = []
    for i in range(rows*2+1):
        row = []
        for j in range(cols*2):
            if i % 2 == 0 or j % 2 == 0:
                row.append(".")
            else:
                row.append(" ")
        grid.append(row)
    return grid

def print_grid(grid):
    print('  1 2 3 4')
    for i in range(len(grid)):
        row = str(i+1) + ' '
        for j in range(len(grid[0])):
            row += grid[i][j] + ' '
        print(row)



def get_boxes(grid):
    boxes = []
    for i in range(1, len(grid)-1, 2):
        for j in range(1, len(grid[0])-1, 2):
            if (grid[i-1][j] == "|" and grid[i+1][j] == "|" and
                grid[i][j-1] == "-" and grid[i][j+1] == "-" and
                grid[i][j] == " "):
                boxes.append((i, j))
    return boxes

def is_game_over(grid):
    for row in grid:
        if " " in row:
            return False
    return True

def update_score(grid, player):
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i % 2 == 0 and j % 2 == 1:
                # horizontal line
                if grid[i][j-1] is not None and grid[i][j+1] is not None and grid[i-1][j] is not None and grid[i+1][j] is not None:
                    if player == 'human':
                        grid[i][j] = 'H'
                    else:
                        grid[i][j] = 'A'
                    score += 1
            elif i % 2 == 1 and j % 2 == 0:
                # vertical line
                if grid[i][j-1] is not None and grid[i][j+1] is not None and grid[i-1][j] is not None and grid[i+1][j] is not None:
                    if player == 'human':
                        grid[i][j] = 'H'
                    else:
                        grid[i][j] = 'A'
                    score += 1
    return score


def ai_move(grid):
    boxes = get_boxes(grid)
    if boxes:
        return random.choice(boxes)
    lines = []
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if grid[i][j] == " ":
                if i % 2 == 0 and j % 2 == 1:
                    if (grid[i-1][j] == "|" and grid[i+1][j] == "|" and
                        grid[i][j-1] == " " and grid[i][j+1] == " "):
                        lines.append((i, j))
                elif i % 2 == 1 and j % 2 == 0:
                    if (grid[i-1][j] == " " and grid[i+1][j] == " " and
                        grid[i][j-1] == "-" and grid[i][j+1] == "-"):
                        lines.append((i, j))
    if lines:
        return random.choice(lines)
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if grid[i][j] == " ":
                if i % 2 == 0 and j % 2 == 1:
                    if (grid[i-1][j] == "|" and grid[i+1][j] == "|" and
                        (grid[i][j-1] == "-" or grid[i][j+1] == "-")):
                        return (i, j)
                elif i % 2 == 1 and j % 2 == 0:
                    if (grid[i-1][j] == " " and grid[i+1][j] == " " and
                        (grid[i][j-1] == "|" or grid[i][j+1] == "|")):
                        return (i, j)
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if grid[i][j] == " ":
                if i % 2 == 0 and j % 2 == 1:
                    return (i, j)
                elif i % 2 == 1 and j % 2 == 0:
                    return (i, j)
    return None


def human_move(grid):
    while True:
        move = input("Enter the row and column numbers of the dot to add a line (e.g. 1,2): ")
       # is_horizontal = input(f'Player {human_move}, horizontal (h) or vertical (v)? ') == 'h'
        row, col = move.split(',')
        row, col = int(row) - 1, int(col) - 1
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            print("Invalid move. Try again.")
        elif grid[row][col] is not None:
            print("Line already exists. Try again.")
        else:
            grid[row][col] = 'H'
            return update_score(grid, 'human')



def play_game():
    grid = create_grid(3, 4)
    human_score, ai_score = 0, 0

    while not is_game_over(grid):
        print_grid(grid)

        human_score += human_move(grid)
        print(f"Human: {human_score}, AI: {ai_score}")

        if is_game_over(grid):
            break

        ai_score += ai_move(grid)
        print(f"Human: {human_score}, AI: {ai_score}")

    print_grid(grid)

    if human_score > ai_score:
        print("Congratulations! You won!")
    elif ai_score > human_score:
        print("Better luck next time! The AI won.")
    else:
        print("It's a tie!")

#play_game()           
