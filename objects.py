import time		
import board
from config import *
from board import *
from images import *
''' This file have classes of all the objects '''
# Main object class which is inherited by ither classes
class Object:

	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def getPosition(self):
		return self.x,self.y

class cloud(Object):

	def __init__(self,x,y):
		super().__init__(x,y)
		self.cloudShape = []
		self.cloudShape.append(['\x1b[1;37;44m'+" "+'\x1b[0m','\x1b[1;37;44m'+" "+'\x1b[0m','\x1b[3;34;47m'+"_"+'\x1b[0m','\x1b[3;34;47m'+"_"+'\x1b[0m','\x1b[1;37;44m'+" "+'\x1b[0m','\x1b[1;37;44m'+" "+'\x1b[0m','\x1b[1;37;44m'+" "+'\x1b[0m'])
		self.cloudShape.append(['\x1b[1;37;44m'+" "+'\x1b[0m','\x1b[3;34;47m'+"_"+'\x1b[0m','\x1b[3;34;47m'+"("+'\x1b[0m','\x1b[3;34;47m'+" "+'\x1b[0m','\x1b[3;34;47m'+")"+'\x1b[0m','\x1b[1;37;44m'+"_"+'\x1b[0m','\x1b[1;37;44m'+" "+'\x1b[0m'])
		self.cloudShape.append(['\x1b[3;34;47m'+"("+'\x1b[0m','\x1b[3;34;47m'+" "+'\x1b[0m','\x1b[3;34;47m'+")"+'\x1b[0m','\x1b[3;34;47m'+"("+'\x1b[0m','\x1b[3;34;47m'+" "+'\x1b[0m','\x1b[3;34;47m'+"~"+'\x1b[0m','\x1b[3;34;47m'+")"+'\x1b[0m'])

	# def getPosition(self):
	# 	return self.x,self.y

	def draw(self,matrix):
		for k in range(3):
			for j in range(len(self.cloudShape[k])):
				matrix[2+k][self.y+j] = self.cloudShape[k][j] 
		


class mario(Object):
	def __init__(self,x=41,y=100):
		super().__init__(x,y)
		self.t = 0
		self.value = 0
		self.jumpStart = 0
		self._jumpit = False
		self.moveForward = True
		self.moveBackword = True
	# def getPosition(self):
	# 	return self.x,self.y
	
	def updatePosition(self,xPlus,yPlus):
		self.x = self.x+xPlus
		self.y = self.y+yPlus

	def draw(self,matrix,colStart):
		matrix[self.x][self.y] = colors['Black']+'('+'\x1b[0m'
		matrix[self.x][self.y+1] = colors['Black']+')'+'\x1b[0m'
		if self.x < 41:
			if (self.x+self.y)%4 == 1:
				matrix[self.x+1][self.y] = '\x1b[6;30;45m' + '<'+'\x1b[0m'
				matrix[self.x+1][self.y+1] = '\x1b[6;30;45m' + '>'+'\x1b[0m'
				matrix[self.x+2][self.y] = '\x1b[6;32;46m' + '/'+'\x1b[0m'
				matrix[self.x+2][self.y+1] = '\x1b[6;32;46m' + '\\'+'\x1b[0m'
			elif (self.x + self.y)%4 == 3: 
				matrix[self.x+1][self.y] = '\x1b[6;30;45m' + '>'+'\x1b[0m'
				matrix[self.x+1][self.y+1] = '\x1b[6;30;45m' + '<'+'\x1b[0m'
				matrix[self.x+2][self.y] = '\x1b[6;32;46m' + '/'+'\x1b[0m'
				matrix[self.x+2][self.y+1] = '\x1b[6;32;46m' + '\\'+'\x1b[0m'
		else:
			if (self.x+self.y)%4 == 1:
				matrix[self.x+1][self.y] = '\x1b[6;30;45m' + '\\'+'\x1b[0m'
				matrix[self.x+1][self.y+1] = '\x1b[6;30;45m' + '/'+'\x1b[0m'
				matrix[self.x+2][self.y] = '\x1b[6;32;46m' + '/'+'\x1b[0m'
				matrix[self.x+2][self.y+1] = '\x1b[6;32;46m' + '\\'+'\x1b[0m'
			elif (self.x+self.y)%4 == 3:
				matrix[self.x+1][self.y] = '\x1b[6;30;45m' + '\\' +'\x1b[0m'
				matrix[self.x+1][self.y+1] = '\x1b[6;30;45m' + '/' +'\x1b[0m'
				matrix[self.x+2][self.y+0] = '\x1b[6;32;46m' + '|'+'\x1b[0m'
				matrix[self.x+2][self.y+1] = '\x1b[6;32;46m' + '|'+'\x1b[0m'
	
	def jump(self,val):
		if self._jumpit:
			return
		self._jumpit = True
		self.jumpStart = self.x
		self.t = self.x
		self.value = val
				

	def Jumping(self):
		self.t += 1
		if self.t-self.jumpStart>0 and self.t-self.jumpStart <= self.value:
			self.x = self.x - 2
		elif self.t-self.jumpStart > self.value and self.t-self.jumpStart <= 2*self.value:
			self.x =  self.x + 2
			if self.x > 41:
				self.x = 41
		else:
			self._jumpit = False
			self.t = 0
			self.x = self.jumpStart

class enemy(Object):

	def __init__(self,x,y):
		super().__init__(x,y)
		self.t = 0;
	# def getPosition(self):
	# 	return self.x,self.y

	def draw(self,matrix):
		self.t += 1
		if int(self.t/30)%2==0:
			self.y += 1
		else:
			self.y -= 1
		if self.y >=5 and self.y < 1400:
			matrix[self.x][self.y] = '\x1b[4;33;41m'+'/'+'\x1b[0m'
			matrix[self.x][self.y+1] = '\x1b[4;33;41m'+'\\'+'\x1b[0m'
			matrix[self.x+1][self.y] = '\x1b[4;33;41m'+'|'+'\x1b[0m'
			matrix[self.x+1][self.y+1] = '\x1b[4;33;41m'+'|'+'\x1b[0m'

class smartEnemy(Object):

	def __init__(self,x,y):
		super().__init__(x,y)
		self.flag = -1
	
	def draw(self,matrix):
		self.y += 4*self.flag
		if self.y%8 == 0 or self.y%8 == 2:
			self.x = 40
		elif self.y%8 == 4 or self.y%8 == 6:
			self.x = 41
		matrix[self.x][self.y] = '\x1b[4;33;42m'+'/'+'\x1b[0m'
		matrix[self.x][self.y+1] = '\x1b[4;33;42m'+'\\'+'\x1b[0m'
		matrix[self.x+1][self.y] = '\x1b[4;33;42m'+'o'+'\x1b[0m'
		matrix[self.x+1][self.y+1] = '\x1b[4;33;42m'+'o'+'\x1b[0m'

class bossEnemy(Object):

	def __init(self,x,y):
		super().__init(x,y)
		
	def draw(self,matrix):
		for i in range(15):
			for j in range(len(shape[i])):
				if shape[i][j] != ' ':
					matrix[self.x+i][self.y+j] = '\x1b[4;31;40m'+shape[i][j]+'\x1b[0m'

class Brick(Object):

	def __init__(self,x,y,flag):
		super().__init__(x,y)
		self.flag = flag
	
	def draw(self,matrix):
		if self.flag>0:
			matrix[self.x][self.y] = '\x1b[0;30;41m'+'B'+'\x1b[0m'
			matrix[self.x][self.y+1] = '\x1b[0;30;41m'+'r'+'\x1b[0m'
			matrix[self.x+1][self.y] = '\x1b[0;30;41m'+'i'+'\x1b[0m'
			matrix[self.x+1][self.y+1] = '\x1b[0;30;41m'+'K'+'\x1b[0m'
		else:
			matrix[self.x][self.y] = '\x1b[5;30;41m'+'/'+'\x1b[0m'
			matrix[self.x][self.y+1] = '\x1b[5;30;41m'+'/'+'\x1b[0m'
			matrix[self.x+1][self.y] = '\x1b[5;30;41m'+'/'+'\x1b[0m'
			matrix[self.x+1][self.y+1] = '\x1b[5;30;41m'+'/'+'\x1b[0m'
		

class pit(Object):
	def __init__(self,x,y):
		super().__init__(x,y)
	
	def draw(self,matrix):
		for i in range(6):
			for j in range(10):
				matrix[self.x+j][self.y+i] = '\x1b[1;37;44m'+' '+'\x1b[0m'

class coin(Object):
	def __init__(self,x,y):
		super().__init__(x,y)

	def draw(self,matrix):
		matrix[self.x][self.y] = '\x1b[6;30;43m'+'$'+'\x1b[0m'

class pipe(Object):

	def __init__(self,x,y):
		super().__init__(x,y)

	def draw(self,matrix):
		
		matrix[self.x][self.y-1] = '\x1b[1;30;42m'+'='+'\x1b[0m'		
		matrix[self.x][self.y] = '\x1b[1;30;42m'+'|'+'\x1b[0m'		
		matrix[self.x][self.y+4] = '\x1b[1;30;42m'+'='+'\x1b[0m'		
		matrix[self.x+1][self.y] = '\x1b[1;30;42m'+'|'+'\x1b[0m'		
		matrix[self.x+2][self.y] = '\x1b[1;30;42m'+'|'+'\x1b[0m'		
		matrix[self.x+3][self.y] = '\x1b[1;30;42m'+'|'+'\x1b[0m'		
		matrix[self.x][self.y+1] = '\x1b[1;30;42m'+'"'+'\x1b[0m'		
		matrix[self.x+1][self.y+1] = '\x1b[1;30;42m'+'-'+'\x1b[0m'		
		matrix[self.x+2][self.y+1] = '\x1b[1;30;42m'+'-'+'\x1b[0m'		
		matrix[self.x+3][self.y+1] = '\x1b[1;30;42m'+'-'+'\x1b[0m'		
		matrix[self.x][self.y+2] = '\x1b[1;30;42m'+'"'+'\x1b[0m'		
		matrix[self.x+1][self.y+2] = '\x1b[1;30;42m'+'-'+'\x1b[0m'		
		matrix[self.x+2][self.y+2] = '\x1b[1;30;42m'+'-'+'\x1b[0m'		
		matrix[self.x+3][self.y+2] = '\x1b[1;30;42m'+'-'+'\x1b[0m'		
		matrix[self.x][self.y+3] = '\x1b[1;30;42m'+'|'+'\x1b[0m'		
		matrix[self.x+1][self.y+3] = '\x1b[1;30;42m'+'|'+'\x1b[0m'		
		matrix[self.x+2][self.y+3] = '\x1b[1;30;42m'+'|'+'\x1b[0m'		
		matrix[self.x+3][self.y+3] = '\x1b[1;30;42m'+'|'+'\x1b[0m'

class spring(Object):

	def __init__(self,x,y):
		super().__init__(x,y)

	def draw(self,matrix):
		matrix[self.x][self.y] = '_'
		matrix[self.x][self.y+1] = '_'
		matrix[self.x+1][self.y] = '|'
		matrix[self.x+1][self.y+1] = '|'


