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

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

# Score Card
# Did I need hints? Yes unfortunately my pivot is failing in leetcode even though I double checked and see no difference in the code
# Did you finish within 30 min? n
# Was the solution optimal? Yes my first solution is optimal but the second could be faster if it didn't fail
# Were there any bugs? Y
#  4 1 3 1 = 2.25
