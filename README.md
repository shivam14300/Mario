
SUPER MARIO CLONE

* This is a simple clone of super mario game *

# Features

* Player have 4 lives at the start of game
* Player can lose life by falling in a pit or if attacked by an enemy
* Player get points for breaking a brick,collecting a coin or killing an enemy
* Player will have 400s in total to complete the level
* Player can walk on bricks and pipe also 
* Game scene is colored for better experience

# Controls

* 'd' -> move forward
* 'a' -> move backward
* 'w' -> jump
* 'q' -> quit
  
# Scoring System

* Collecting a coin -> 10 points
* Breaking a brick -> 20 points
* Killing normal enemy -> 30 points
* Killing strong enemy -> 60 points(counted as 2 kills)

# Running the program

    $- python3 main.py

# File Structure

    .
    ├── board.py
    ├── config.py
    ├── images.py
    ├── main.py
    ├── objects.py
    ├── README.md
    └── requirements.txt

# Detail about Different Objects

    1. Smart Enemy:-
        1.1 It moves in a zig-zag manner
        1.2 It moves faster than normal enemy
        1.3 It oscillates in a range()
        1.4 Killing it is very difficult

    2. Bricks:-
        2.1 Different bricks have different points
        2.2 Player can take points while it doesn't change its character

    3. Spring:-
        3.1 If player lands on the spring it can jump very high

# List of Objects

1. Mario
2. Enemy
3. Smart Enemy
4. Brick
5. Pit
6. Pipe
7. Coins
8. Spring
