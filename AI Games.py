import random
from collections import deque
import heapq
import time


# Maze Game (BFS)


maze_lab2 = [
    ['S', '.', '.', '#'],
    ['#', '#', '.', '#'],
    ['.', '.', '.', 'G']
]

ROWS = len(maze_lab2)
COLS = len(maze_lab2[0])

def find_symbol(symbol):
    for r in range(ROWS):
        for c in range(COLS):
            if maze_lab2[r][c] == symbol:
                return (r, c)
    return None

START = find_symbol('S')
GOAL  = find_symbol('G')

ACTIONS = {
    'up':    (-1, 0),
    'down':  ( 1, 0),
    'left':  ( 0,-1),
    'right': ( 0, 1)
}

def in_bounds(pos):
    r, c = pos
    return 0 <= r < ROWS and 0 <= c < COLS

def is_free(pos):
    r, c = pos
    return maze_lab2[r][c] != '#'

def get_neighbors_bfs(pos):
    neighbors = []
    for action in ['up','down','left','right']:
        dr, dc = ACTIONS[action]
        nr, nc = pos[0] + dr, pos[1] + dc
        npos = (nr, nc)
        if in_bounds(npos) and is_free(npos):
            neighbors.append(npos)
    return neighbors

def reconstruct_path(parent, start, goal):
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    path.reverse()
    return path

def bfs(start, goal):
    queue = deque([start])
    visited_set = set([start])
    parent = {start: None}
    visited_order = []

    while queue:
        cur = queue.popleft()
        visited_order.append(cur)
        if cur == goal:
            path = reconstruct_path(parent, start, goal)
            return path, visited_order

        for nbr in get_neighbors_bfs(cur):
            if nbr not in visited_set:
                visited_set.add(nbr)
                parent[nbr] = cur
                queue.append(nbr)
    return None, visited_order

def print_maze_with_path_lab2(path):
    display = [row[:] for row in maze_lab2]
    if path:
        for (r, c) in path:
            if display[r][c] not in ('S', 'G'):
                display[r][c] = '*'
    return "\n".join(' '.join(row) for row in display)

def maze_bfs_dfs():
    print("Maze (Lab 2 BFS):")
    print(print_maze_with_path_lab2(None))
    print("\nRunning BFS from start to goal...")
    path, visited = bfs(START, GOAL)
    if path:
        print("\nPath found:", path)
        print("Number of nodes visited:", len(visited))
        print("Visited nodes (in order):", visited)
        print("\nMaze with path marked ('*'):\n")
        print(print_maze_with_path_lab2(path))
    else:
        print("No path found.")


# Maze Game (A*)


maze_lab3 = [
    ['S', '.', '.', '#'],
    ['#', '#', '.', '#'],
    ['.', '.', '.', 'G']
]

start_lab3 = (0, 0)  # S
goal_lab3 = (2, 3)   # G

def heuristic(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def get_neighbors_astar(pos):
    neighbors = []
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        r, c = pos[0] + dr, pos[1] + dc
        if 0 <= r < len(maze_lab3) and 0 <= c < len(maze_lab3[0]) and maze_lab3[r][c] != '#':
            neighbors.append((r, c))
    return neighbors

def a_star():
    open_list = [(0, start_lab3)]  
    came_from = {}
    g_score = {start_lab3: 0}
    visited = set()

    while open_list:
        f, current = heapq.heappop(open_list)

        if current == goal_lab3:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start_lab3)
            path.reverse()
            return path, len(visited)

        if current in visited:
            continue
        visited.add(current)

        for neighbor in get_neighbors_astar(current):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal_lab3)
                heapq.heappush(open_list, (f_score, neighbor))

    return None, len(visited)

def print_path_astar(path):
    if not path:
        return ""
    display = [row[:] for row in maze_lab3]
    for r, c in path:
        if maze_lab3[r][c] == '.':
            display[r][c] = '*'
    return "\n".join(' '.join(row) for row in display)

def maze_a_star():
    print("Maze (Lab 3 A*):")
    print("\nRunning A* search...")
    start_time = time.time()
    path, nodes_expanded = a_star()
    end_time = time.time()

    if path:
        print("\nPath found:", path)
        print("Path cost:", len(path) - 1)
        print("Nodes expanded:", nodes_expanded)
        print("Time: {:.6f} seconds".format(end_time - start_time))
        print("\nMaze with path:\n")
        print(print_path_astar(path))
    else:
        print("No path found!")


#  Tic Tac Toe (8x8 Connect-4)


# Tic Tac Toe (8x8 Connect-4)

def check_win_8x8(board, player):
    # Wrapper for 8x8 game with 4-in-a-row
    return check_win(board, player, 4)

def make_move(board, row, col, player):
    if 0 <= row < len(board) and 0 <= col < len(board) and board[row][col] == '.':
        board[row][col] = player
        return True
    return False

def ai_move_8x8(board):
    for r in range(8):
        for c in range(8):
            if board[r][c] == '.':
                board[r][c] = 'O'
                if check_win_8x8(board, 'O'):
                    return
                board[r][c] = '.'

    for r in range(8):
        for c in range(8):
            if board[r][c] == '.':
                board[r][c] = 'X'
                if check_win_8x8(board, 'X'):
                    board[r][c] = 'O'
                    return
                board[r][c] = '.'

    empty_cells = [(r, c) for r in range(8) for c in range(8) if board[r][c] == '.']
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = 'O'

def tic_tac_toe():
    board = [['.' for _ in range(8)] for _ in range(8)]
    print("Welcome to 8x8 Tic Tac Toe (Connect-4 variant)!")
    print("You are X, AI is O. Get 4 in a row to win.\n")
    print_board(board)

    while True:
        try:
            raw = input("Enter your move (row col): ")
            row, col = map(int, raw.split())
        except Exception:
            print("Please enter two numbers separated by space (e.g., 3 4).")
            continue

        if not make_move(board, row, col, 'X'):
            print("Invalid move. Try again.")
            continue

        print_board(board)
        if check_win_8x8(board, 'X'):
            print("You win!")
            break

        if all(board[r][c] != '.' for r in range(8) for c in range(8)):
            print("It's a draw!")
            break

        ai_move_8x8(board)
        print("AI move:")
        print_board(board)
        if check_win_8x8(board, 'O'):
            print("AI wins!")
            break

        if all(board[r][c] != '.' for r in range(8) for c in range(8)):
            print("It's a draw!")
            break



#  Bonus Challenge


import random


def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_win(board, player, win_n):
    n = len(board)
    for r in range(n):
        for c in range(n):
           
            if c + win_n - 1 < n and all(board[r][c+i] == player for i in range(win_n)):
                return True
           
            if r + win_n - 1 < n and all(board[r+i][c] == player for i in range(win_n)):
                return True
           
            if r + win_n - 1 < n and c + win_n - 1 < n and all(board[r+i][c+i] == player for i in range(win_n)):
                return True
            
            if r + win_n - 1 < n and c - win_n + 1 >= 0 and all(board[r+i][c-i] == player for i in range(win_n)):
                return True
    return False

def score_board(board, player, win_n):
   
    opponent = 'O' if player == 'X' else 'X'
    score = 0
    n = len(board)
    for r in range(n):
        for c in range(n):
            directions = [(0,1),(1,0),(1,1),(1,-1)]
            for dr, dc in directions:
                line = []
                for i in range(win_n):
                    rr, cc = r + dr*i, c + dc*i
                    if 0 <= rr < n and 0 <= cc < n:
                        line.append(board[rr][cc])
                    else:
                        break
                if len(line) == win_n:
                    if opponent not in line:
                        score += line.count(player)
    return score

def minimax_simple(board, depth, maximizing, win_n):
    if check_win(board, 'O', win_n):
        return 100
    if check_win(board, 'X', win_n):
        return -100
    if depth == 0 or all(cell != '.' for row in board for cell in row):
        return score_board(board, 'O', win_n)
    
    if maximizing:
        best = -float('inf')
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    board[r][c] = 'O'
                    val = minimax_simple(board, depth-1, False, win_n)
                    board[r][c] = '.'
                    best = max(best, val)
        return best
    else:
        best = float('inf')
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    board[r][c] = 'X'
                    val = minimax_simple(board, depth-1, True, win_n)
                    board[r][c] = '.'
                    best = min(best, val)
        return best

def ai_move(board, win_n):
    best_score = -float('inf')
    best_move = None
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == '.':
                board[r][c] = 'O'
                score = minimax_simple(board, 2, False, win_n)  
                board[r][c] = '.'
                if score > best_score:
                    best_score = score
                    best_move = (r,c)
    if best_move:
        board[best_move[0]][best_move[1]] = 'O'

def tic_tac_toe_Bonus():
    try:
        size = int(input("Enter board size (e.g., 5 for 5x5): "))
        win_n = int(input("Enter win condition (e.g., 4 for 4-in-a-row): "))
    except:
        print("Invalid input, using default 8x8 and 4-in-a-row.")
        size = 8
        win_n = 4

    board = [['.' for _ in range(size)] for _ in range(size)]
    print(f"Welcome to {size}x{size} Connect-{win_n}!")
    print("You are X, AI is O.\n")
    print_board(board)

    while True:
        
        try:
            row, col = map(int, input("Enter your move (row col): ").split())
        except:
            print("Invalid input. Enter row and column numbers separated by space.")
            continue
        if not (0 <= row < size and 0 <= col < size) or board[row][col] != '.':
            print("Invalid move. Try again.")
            continue

        board[row][col] = 'X'
        print_board(board)
        if check_win(board, 'X', win_n):
            print("You win!")
            break

        if all(cell != '.' for row in board for cell in row):
            print("It's a draw!")
            break

      
        ai_move(board, win_n)
        print("AI move:")
        print_board(board)
        if check_win(board, 'O', win_n):
            print("AI wins!")
            break

        if all(cell != '.' for row in board for cell in row):
            print("It's a draw!")
            break






# Menu for Lab 2, 3, 4 and  Bonus Challenge

def main():
    while True:
        print("\nSelect a game to play:")
        print("1. Maze Game (BFS/DFS)")
        print("2. Maze Game (A*)")
        print("3. Tic Tac Toe (8x8 Connect-4)")
        print("4. Tic Tac Toe Bonus Challenge")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            maze_bfs_dfs()
        elif choice == "2":
            maze_a_star()
        elif choice == "3":
            tic_tac_toe()
        elif choice == "4":
            tic_tac_toe_Bonus()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


# Run Program

if __name__ == "__main__":
    main()
