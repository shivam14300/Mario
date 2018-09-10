import board
import objects
import datetime
import config
from board import *
from config import *
''' Main file for running the code '''
bd = board.Board()
p_input = -1
while (True):

    global lives
    p_input = config.get_key(config.get_input())
    if p_input == config.QUIT: # if input is q, quit the game 
        break
    # Calling collision function
    bd.CollisionMarioPipe()
    bd.process_input(p_input)
    bd.insert()
    bd.printIt()
    flag1 = bd.CollisionMarioBrick()
    flag = bd.CollisionMarioEnemy()
    flag2 = bd.CollisionMarioSmartEnemy()
    bd.CollisionMarioCoin()
    bd.CollisionMarioSpring()
    
    if bd.youWin():
        break

    if board.t == 0:
        bd.gameOver()
        break
    
    if flag == -1 or flag1 == -1 or flag2 == -1:
    
        if board.lives == 1:
            bd.gameOver()
            break

    # RESPAWNING    
        board.lives -= 1
        mario.x = 41
        mario.y = 100
        board.colStart = 0
        board.colEnd = 200