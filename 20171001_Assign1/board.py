import sys
# import time
from time import time
# import os
import config
import objects
from objects import *
# from config import *
from images import *
from os import system
from random import randint
''' Complete file for board and creating objects on the board  '''
scoreCoin = 0
scoreBrick = 0
scoreEnemy = 0
lives = 4
Rows = 55 
Cols = 650 # Length of total arena
colStart = 0
colEnd = 200 # Length of arena printed
t = 400
Time = time()
score = 0

mario = objects.mario() #Player mario is created

#matrix for printing the game is created
matrix = []
for i in range(Rows):
	matrix.append([' ']*Cols)

#creating clouds
clouds = []
for i in range(30):
	clouds.append(cloud(2,randint(1,500)))

#creating bricks and coins
bricks = []
coins = []
for i in range(6):
	for j in range(5):
		bricks.append(Brick(36,70*(i+1)+2*j,randint(1,5)))
		coins.append(coin(30,70*(i+1)+2*j+1))
	for j in range(3):
		bricks.append(Brick(36,30+70*(i+1)+2*j,randint(1,5)))
		coins.append(coin(30,30+70*(i+1)+2*j+1))

for i in range(6):
	if i%2:
		coins.append(coin(35,50+70*(i+1)+1))
		coins.append(coin(36,50+70*(i+1)-1))
		coins.append(coin(36,50+70*(i+1)+3))
		coins.append(coin(37,50+70*(i+1)-1))
		coins.append(coin(37,50+70*(i+1)+3))
		coins.append(coin(38,50+70*(i+1)+1))
	else:
		coins.append(coin(28,50+70*(i+1)+1))
		coins.append(coin(29,50+70*(i+1)-1))
		coins.append(coin(29,50+70*(i+1)+3))
		coins.append(coin(30,50+70*(i+1)-1))
		coins.append(coin(30,50+70*(i+1)+3))
		coins.append(coin(31,50+70*(i+1)+1))



#creating Pits
pits = []
for i in range(8):
	if i%2:
		pits.append(pit(44,60*(i+1)-15))

#creating pipes and enemies
pipes = []
enemies = []
for i in range(5):
	pipes.append(pipe(40,60*(i+2)))
	coins.append(coin(39,60*(i+2)+0))
	coins.append(coin(39,60*(i+2)+3))
	enemies.append(enemy(42,60*(i+2)+4))

#creating smart Enemies
smartEnemies = []
for i in range(5):
	smartEnemies.append(smartEnemy(41,2*randint(150,250)))

#creating springs
springs = []
springs.append(spring(42,490))
springs.append(spring(42,390))
springs.append(spring(42,190))

bossEnemies = []
# bossEnemies.append(bossEnemy(29,500))


# Main board class
class Board():
	global scoreCoin
	global scoreEnemy
	global scoreBrick
	# Function for processing the input of the keyboard
	def process_input(self, key_press):
		
		global colEnd
		global colStart
		marioX,marioY = mario.getPosition()
		if key_press in config.DIR:
			if key_press == config.LEFT and marioY >= colStart + 2:
				if self.CollisionMarioPipe() != -1:
						mario.updatePosition(0,-2)
			
			elif key_press == config.RIGHT and colEnd <= 648:
				if self.CollisionMarioPipe() != 1:
					if marioY == (colStart + colEnd)/2:
						colEnd += 2
						colStart += 2
					else:
						mario.updatePosition(0,2)
			
			elif key_press == config.UP:
				mario.jump(5)

	#Function for inserting different Objects
	def insert(self):
	
		if mario._jumpit:
			mario.Jumping()
	
	# Frist clearing the screen
		for i in range(Rows-1):
			for j in range(colStart,colEnd):
				matrix[i][j]= '\x1b[1;37;44m'+' '+'\x1b[0m'

	# Adding floor`
		for i in range(Rows-11,Rows-1):
			for j in range(colStart,colEnd):
				matrix[i][j] = '\x1b[1;33;43m'+'L'+'\x1b[0m'

	# Adding Terace
		for i in range(colStart,colEnd):
			matrix[0][i] = '\x1b[1;36;43m'+'*'+'\x1b[0m'

	# Adding clouds
		for i in clouds:
			i.draw(matrix)

	# Adding enemies
		if len(enemies) > 0:
			for i in enemies:
				i.draw(matrix)

	# Adding smart enemies
		if len(smartEnemies) > 0:
			for i in smartEnemies:
				if i.y < 8:
					i.flag = 1
				elif i.y > 520:
					i.flag = -1 
				i.draw(matrix)

	# Adding bricks
		for i in bricks:
			i.draw(matrix)
		
	# Adding pits
		for i in pits:
			i.draw(matrix)
		
	# Adding coins
		for i in coins:
			i.draw(matrix)
		
	# Adding pipes
		for i in pipes:
			i.draw(matrix)

	# Adding springs
		for i in springs:
			i.draw(matrix)

		# for i in bossEnemies:
		# 	i.draw(matrix)
	
	# Adding Castle		
		for i in range(20):
			for j in range(len(castle[i])):
				if castle[i][j] != ' ':
					matrix[24+i][530+j] = '\x1b[2;33;41m'+castle[i][j]+'\x1b[0m'

	# Adding mario
		mario.draw(matrix,colStart)

	# Function to check collision of mario and enemy
	def CollisionMarioEnemy(self):
		global scoreEnemy
		marioX,marioY = mario.getPosition()
		for i in enemies:
			enemyX,enemyY = i.getPosition()
			if marioX+3 == enemyX and marioY == enemyY or marioX+3 == enemyX and marioY+1 == enemyY or marioX+3 == enemyX and marioY-1 == enemyY:
				enemies.remove(i)
				scoreEnemy += 1
			if marioX+1==enemyX and marioY+2==enemyY or marioX+2==enemyX and marioY+2==enemyY:
				return -1
	
	# Function to check collision of mario and smart enemy
	def CollisionMarioSmartEnemy(self):
		global scoreEnemy
		marioX,marioY = mario.getPosition()
		for i in smartEnemies:
			enemyX,enemyY = i.getPosition()
			if marioX+1 == enemyX and marioY == enemyY or marioX+1 == enemyX and marioY == enemyY+1 or marioX+1 == enemyX and marioY == enemyY-1:
				smartEnemies.remove(i)
				scoreEnemy += 2
			if marioX==enemyX and marioY+5==enemyY or marioX==enemyX and marioY+4==enemyY or marioX==enemyX and marioY+3==enemyY or marioX==enemyX and marioY+2==enemyY:
				return -1
	
	# Function to check collision of mario and coin
	def CollisionMarioCoin(self):
		global scoreCoin
		marioX,marioY = mario.getPosition()
		for i in coins:
			coinX,coinY = i.getPosition()
			if marioX == coinX and marioY == coinY or marioX+1 == coinX and marioY == coinY or marioX+2 == coinX and marioY == coinY or marioX == coinX and marioY+1 == coinY or marioX+1 == coinX and marioY+1 == coinY or marioX+2 == coinX and marioY+1 == coinY:
				coins.remove(i)
				scoreCoin += 1

	# Function to check collision of mario and brick
	def CollisionMarioBrick(self):
		global scoreBrick
		marioX,marioY = mario.getPosition()
		for i in bricks:
			brickX,brickY = i.getPosition()
			if marioX+3 == brickX and marioY+1 == brickY or marioX+3 == brickX and marioY == brickY or marioX+3 == brickX and marioY-1 == brickY:
				mario._jumpit = False
			if marioX == brickX+1 and marioY == brickY or marioX == brickX+1 and marioY == brickY +1 or marioX == brickX+1 and marioY == brickY-1:
				if i.flag > 0:
					i.flag -= 1
					scoreBrick += 1
				mario.t += 4
			elif mario._jumpit == False and matrix[marioX+3][marioY] == '\x1b[1;37;44m'+' '+'\x1b[0m' and matrix[marioX+3][marioY+1] == '\x1b[1;37;44m'+' '+'\x1b[0m':
				if mario.x == 41:
					return -1
				mario.jumpStart = 41
				mario.t = 46
				mario.value = 5
				mario._jumpit = True
	
	# Function to check collision of mario and pipe
	def CollisionMarioPipe(self):
		marioX,marioY = mario.getPosition()
		flag = 0
		for i in pipes:
			pipeX,pipeY = i.getPosition()
			if marioX+3 == pipeX and marioY+1 == pipeY or marioX+3 == pipeX and marioY == pipeY or marioX+3 == pipeX and marioY-1 == pipeY or marioX+3 == pipeX and marioY-2 == pipeY or marioX+3 == pipeX and marioY+2 == pipeY:
				mario._jumpit = False
			if marioX-1 == pipeX and marioY+2 == pipeY or marioX-1 == pipeX and marioY+1 == pipeY or marioX == pipeX and marioY+2 == pipeY or marioX == pipeX and marioY+1 == pipeY or marioX+1 == pipeX and marioY+2 == pipeY or marioX+1 == pipeX and marioY+1 == pipeY or marioX+2 == pipeX and marioY+2 == pipeY or marioX+2 == pipeX and marioY+1 == pipeY:
				flag = 1
			elif marioX-1 == pipeX and marioY == pipeY+4 or marioX-1 == pipeX and marioY == pipeY+4 or marioX == pipeX and marioY == pipeY+4 or marioX == pipeX and marioY == pipeY+4 or marioX+1 == pipeX and marioY == pipeY+4 or marioX+1 == pipeX and marioY == pipeY+4 or marioX+2 == pipeX and marioY == pipeY+4 or marioX == pipeX and marioY+1 == pipeY+4:
				flag = -1
		return flag

	# Function to check collision of mario and enemy
	# def CollisionEnemyPit(self):
	# 	for i in enemies:
	# 		enemyX,enemyY = i.getPosition()
	# 		for j in pits:
	# 			pitX,pitY = j.getPosition()
	# 			if matrix[enemyX+2][enemyY] == '\x1b[1;37;44m'+' '+'\x1b[0m' or matrix[enemyX+2][enemyY+1] == '\x1b[1;37;44m'+' '+'\x1b[0m' or matrix[enemyX+1][enemyY+1] == '\x1b[1;37;44m'+' '+'\x1b[0m' or matrix[enemyX+1][enemyY] == '\x1b[1;37;44m'+' '+'\x1b[0m':
	# 				enemies.remove(i)

	# Function to check collision of mario and spring
	def CollisionMarioSpring(self):
		marioX,marioY = mario.getPosition()
		for i in springs:
			springX,springY = i.getPosition()
			if marioX+1 == springX and marioY == springY or marioX+1 == springX and marioY+1 == springY or marioX+1 == springX and marioY-1 == springY:
				mario.jump(20) 

	# Printing the board
	def printIt(self):
		global scoreCoin	
		global scoreBrick	
		global scoreEnemy	
		global matrix
		sys.stdout.flush()
		try:
			system('clear')
		except BaseException:
			system('cls')
		print('Coins: {}  Bricks: {}  Enemy: {}  Lives: {}  Time: {}'.format(scoreCoin,scoreBrick,scoreEnemy,lives,int(t-(time()-Time))))
		for i in range(Rows-1):
			for j in range(colStart,colEnd):
				print(matrix[i][j],end = '')
			print('')
	
	# Check if player completed the game
	def youWin(self):
		if mario.y == 546 or mario.y == 545 or mario.y == 544:
			for i in range(6):
				for j in range(len(win[i])):
					print(win[i][j],end='')
				print('')
			print('')
			print('')
			print("                                              Coins Collected {} X 10".format(scoreCoin))
			print("                                               Bricks Breaked {} X 20".format(scoreBrick))
			print("                                                 Enemy Killed {} X 30".format(scoreEnemy))
			print("                                                    Time Left {} X 1".format(int(t-(time()-Time))))
			print("                                                 Total Score: {}".format(scoreCoin*10 + scoreBrick*20 + scoreEnemy*30))
			return True
        	
	# Check if player lost the game
	def gameOver(self):
		
		global scoreCoin	
		global scoreBrick	
		global scoreEnemy	
		for i in range(4):
			for j in range(len(over[i])):
				print(over[i][j],end='')
			print('')
		print('')
		print('')
		print("                                              Coins Collected {} X 10".format(scoreCoin))
		print("                                               Bricks Breaked {} X 20".format(scoreBrick))
		print("                                                 Enemy Killed {} X 30".format(scoreEnemy))
		print("                                                 Total Score: {}".format(scoreCoin*10 + scoreBrick*20 + scoreEnemy*30 ))
        