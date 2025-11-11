This Python program combines multiple AI search algorithms and game implementations. It provides a menu-based interface where users can choose between maze pathfinding algorithms (BFS and A*), or play an AI-powered Tic Tac Toe game (Connect-4 variant).

-Features

-BFS Pathfinding: Finds the shortest path in a maze using breadth-first search.

-A* Algorithm: Uses a heuristic (Manhattan distance) for optimal pathfinding.

-Tic Tac Toe (8x8): A variant of Connect-4 where you compete against an AI opponent.

-Bonus Mode: Customizable Tic Tac Toe with adjustable board size and win condition, powered by a simple Minimax strategy.

-AI Decision Making: AI tries to block you or find the best move dynamically.

-Text-Based Interface: Simple CLI navigation.



How it works

1. Maze Game (BFS)

Uses a queue (FIFO) structure to explore neighboring cells layer by layer.

Ensures the shortest path from start (S) to goal (G) is found.

Displays the explored nodes and the final path marked with *.

2. Maze Game (A)*

Combines path cost and heuristic (Manhattan distance).

Uses a priority queue (heapq) for efficient node expansion.

Displays the total path cost, nodes expanded, and execution time.

3. Tic Tac Toe (8x8 Connect-4)

Win by forming 4 in a row horizontally, vertically, or diagonally.

The AI makes logical or random moves based on board evaluation.

4. Bonus Challenge (Dynamic Connect-N)

Lets you choose:

Board size (e.g., 5x5, 8x8, etc.)

Win condition (e.g., 3-in-a-row, 4-in-a-row, etc.)

Implements a simplified Minimax algorithm with scoring evaluation.


-Installation

Clone or download the project: e.g

git clone https://github.com/yourusername/ai-lab-games.git
cd ai-lab-games


Ensure you have Python 3.8+ installed:
