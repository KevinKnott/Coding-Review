#  Design Snake Game: https://leetcode.com/problems/design-snake-game/

# Design a Snake game that is played on a device with screen size height x width. Play the game online if you are not familiar with the game.
# The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.
# You are given an array food where food[i] = (ri, ci) is the row and column position of a piece of food that the snake can eat. When a snake eats a piece of food, its length and the game's score both increase by 1.
# Each piece of food appears one by one on the screen, meaning the second piece of food will not appear until the snake eats the first piece of food.
# When a piece of food appears on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
# The game is over if the snake goes out of bounds (hits a wall) or if its head occupies a space that its body occupies after moving (i.e. a snake of length 4 cannot run into itself).

# Implement the SnakeGame class:

# SnakeGame(int width, int height, int[][] food) Initializes the object with a screen of size height x width and the positions of the food.
# int move(String direction) Returns the score of the game after applying one direction move by the snake. If the game is over, return -1.
from collections import deque


class SnakeGame:

    def __init__(self, width: int, height: int, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        # self.grid = [['.'] * width  for _ in range(height)]
        self.height = height
        self.width = width
        self.food = deque()
        self.score = 0
        self.snake = deque()
        self.snake.appendleft([0, 0])

        for r, c in food:
            self.food.appendleft((r, c))

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        dir = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}

        # Check if the direction plus top of q is out of bounds
        curRow, curCol = self.snake[0]
        nextRow, nextCol = curRow + \
            dir[direction][0], curCol + dir[direction][1]

        if nextRow < 0 or nextRow >= self.height:
            return -1

        if nextCol < 0 or nextCol >= self.width:
            return -1

        if [nextRow, nextCol] in self.snake and [nextRow, nextCol] != self.snake[-1]:
            return -1

        self.snake.appendleft([nextRow, nextCol])

        if len(self.food) and (nextRow, nextCol) == self.food[-1]:
            self.food.pop()
            self.score += 1

        while len(self.snake) > self.score + 1:
            self.snake.pop()

        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

# My code is optimized to be run in o(1) time and o( N + W * H) where N is food and W * H is the snake set structure
#

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Yes my first solution is optimal
# Were there any bugs? Yup I forgot to make sure my check for hitting the boddy comes after we have removed the last element
#  5 3 5 3 = 4
