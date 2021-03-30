import pygame
import random
pygame.mixer.pre_init()

pygame.init()

screen = pygame.display.set_mode((800, 450))


def displayText(surface,message,x,y,size,r,g,b):
	myfont = pygame.font.Font(None,size)
	textImage = myfont.render(message, True, (r,g,b))
	surface.blit(textImage,(x,y))


class player():
	"""docstring for player"""
	def __init__(self):
		# self.image = pygame.Surface([100, 400])

		#images
		self.images = []
		self.images.append(pygame.image.load('player-1.png'))
		self.images.append(pygame.image.load('player-2.png'))
		self.index = 0
		self.image = self.images[self.index]

		self.rect = self.image.get_rect()
		self.rect.x = 125
		self.rect.y = 156

		# self.image.fill((255, 0, 0))

		self.speed_x=12


		self.floor = 156


		self.jump = False
		self.speed_y=11
		self.mass = 1


		self.shift = False

		self.power = 100
		self.power_max=100

	def render(self,collision):
		pressed = pygame.key.get_pressed()
		# if pressed[pygame.K_UP]: self.rect[1] -= self.speed_y

		if pressed[pygame.K_LEFT]: self.rect[0] -= self.speed_x
		if pressed[pygame.K_RIGHT]: self.rect[0] += self.speed_x


		if collision ==True:
			# self.rect.x+=1
			if self.speed_x>=0:
				self.speed_x = 0
			else:
				self.speed_x = 20
		else:
			self.speed_x = 20

		# print(self.rect)
		screen.blit(self.image, self.rect)


	def update(self):
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]

	def leap(self,collision,obstacle_height):
		pressed = pygame.key.get_pressed()

		if self.jump==False:
			self.power+=0.1
			if self.power >= self.power_max:
				self.power = self.power_max

			if pressed[pygame.K_UP]:
				# print("jump")
				self.power-=10
				self.jump=True

		if self.jump==True:
			F =(1 / 2)*self.mass*(self.speed_y**2)

			self.rect[1]-= F

			self.speed_y -=1.25

			if self.speed_y<=0:

				self.mass = -1

			if self.speed_y <=-11:

				self.jump = False

				self.speed_y=11

				self.mass=1
				if collision==True:

					self.rect.y = 281-obstacle_height
					# print(self.rect.y)
					
				else:
					self.rect.y = self.floor
		# print(self.power)
	def crouch(self,collision):
		self.shift=False
		pressed = pygame.key.get_pressed()
		if self.shift==False:
			if pressed[pygame.K_DOWN]:
				self.shift=True
				# print("key down")
			else:
				self.shift=False
				# print("false")
		if self.shift==True:
			#shrink
			# print("shift")
			pass


class obstacle():
	"""docstring for obstacle"""
	def __init__(self):

		self.image = pygame.image.load('apple.png')
		self.rect = self.image.get_rect()
		self.rect.x = 800
		self.rect.y = 450
		self.speed = 12.5
		


	def render(self,collision):

		if self.rect[0]<=0:
			self.rect[0]=800-+self.rect[2]
		# print(self.rect)
		if collision ==True:
			# self.rect.x+=1
			self.speed = 0
			# print(self.rect[3])
			return self.rect[3]#height
		else:
			self.rect[0] -= 12.5
		screen.blit(self.image, self.rect)


class background():
	"""docstring for backgro"""
	def __init__(self, x,y,scroll_speed,image,score_counter):





		self.x=x
		self.y=y
		self.scroll_speed = scroll_speed
		self.image =pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.meters_traveled = 0
		self.scroll_speed_bank = scroll_speed

		self.score_counter = score_counter
		
	def draw(self,screen,collision):

		self.x-=self.scroll_speed
		self.meters_traveled+=self.scroll_speed/100
<<<<<<< HEAD
=======

>>>>>>> parent of c2848db (frixed broken background)


		if self.x<=-800:
			self.x=800

		screen.blit(pygame.transform.scale(self.image,(800,450)),(self.x,self.y))

<<<<<<< HEAD
		# screen.blit(pygame.transform.scale(blackTexture, (800, 600)), (0, 0))

=======
>>>>>>> parent of c2848db (frixed broken background)
		if self.score_counter == True:
			displayText(screen,str("%.2f"%self.meters_traveled)+" meters",1000,25,60,255,0,0)

		if collision==True:
			self.scroll_speed=0

		else:
			self.scroll_speed =self.scroll_speed_bank

		# print(self.meters_traveled)
		return self.meters_traveled


class police():
	"""docstring for police"""
	def __init__(self):

		self.speed = 0.006
		self.meters_traveled = -3

		self.images = []
		self.images.append(pygame.image.load('police-1.png'))
		self.images.append(pygame.image.load('police-2.png'))
		self.index = 0
		self.image = self.images[self.index]

		self.rect = self.image.get_rect()

		self.rect.x = -125

		self.rect.y = 156

	def chase(self,player_meters_traveled,collision):
		self.meters_traveled+=self.speed/100
		# print(self.meters_traveled)

		
		if collision==True:
			self.rect[0]+=self.speed + 3
		else:
			self.rect[0]+= 0.006

		# print(self.rect[0])
		screen.blit(self.image, self.rect)
		# if self.meters_traveled>=player_meters_traveled:
		# 	print("lose")

	def update(self):
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]



class text_game():
	"""docstring for text_game"""
	def __init__(self):
		self.font = pygame.font.Font(None, 80)
		self.color = pygame.Color('dodgerblue2')
		self.text = ""
		self.txt_surface = self.font.render(self.text, True, self.color)
		self.rect = self.txt_surface.get_rect()
		self.x = self.rect[2]#
		self.length = 0

	def game(self,event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				print(self.text)
				self.text = ""
			elif event.key == pygame.K_BACKSPACE:
				self.text = self.text[:-1]
			else:
				self.text += event.unicode

	def draw(self):
		self.rect = self.txt_surface.get_rect()
		self.txt_surface = self.font.render(self.text, True, self.color)
		screen.blit(self.txt_surface, ((800/2)-self.rect[2]/2, 600))






def running_game(screen):

	me = player()
	poop = obstacle()
	chasers = police()
	# background_1 = background(0,0,5)
	# background_2 = background(800,0,5)

	city_back1a = background(0,0,5,"city_back1.png",False)
	player_meters_traveled = city_back1b = background(800,0,5,"city_back1.png",True)

	city_back2a = background(0,0,1,"city_back2.png",False)
	city_back2b = background(800,0,1,"city_back2.png",False)
	grass = background(0,0,20,"grass.png",False)

	typing = text_game()

	clock = pygame.time.Clock()

	done = False
	collision = False

	get_caught = False

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

			typing.game(event)

		# background_1.draw(screen,collision)
		#  background_2.draw(screen,collision)
		
		screen.fill((50,50,50))

		city_back2a.draw(screen,collision)
		city_back2b.draw(screen,collision)


		city_back1a.draw(screen,collision)
		player_meters_traveled =city_back1b.draw(screen,collision)


		grass.draw(screen,collision)
		
		
		me.render(collision)

		me.update()

		obstacle_height = poop.render(collision)
		me.leap(collision,obstacle_height)
		me.crouch(collision)

		chasers.chase(player_meters_traveled,collision)
		chasers.update()


		typing.draw()


		if me.rect.colliderect(poop.rect):

			collision = True
		else:
			collision = False

		if me.rect.colliderect(chasers.rect):
			get_caught = True
			quit()		
		else:
			get_caught = False


		# print(screen)
		# print(collision)
		clock.tick(30)

		pygame.display.flip()

# class cutscene():
# 	"""docstring for cutscene"""
# 	def __init__(self):
# 		self.arg = arg
		





cutscene_1 = pygame.image.load("cutscene_1.png")
cutscene_1text = pygame.image.load("cutscene_1b.png")
cutscene_2 = pygame.image.load("cutscene_2.png")
cutscene_3 = pygame.image.load("cutscene_3.png")

width = 800
height = 450

text_x = 800
text_speed = 5
text_accel = 0.1
def cutscene(screen,width,height,text_x,text_speed,text_accel):
	pygame.mixer.music.load("national_anthem.mp3")
	pygame.mixer.music.play(-1,0.0)
	done = False
	zoom_speed = 0.00001#0.004
	zoom_accel = 0.00001
	zoom_accel_out = 0.02
	clock = pygame.time.Clock()

	# pygame.transform.scale(width, height)
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		x=((800/2)-(width/2))		
		y=((450/2)-(height/2))




		screen.blit(pygame.transform.scale(cutscene_1,(width,height)),(x,y))
		screen.blit(cutscene_1text,(text_x,380))

		width+=int(width*zoom_speed)
		height+=int(height*zoom_speed)

		zoom_speed+=zoom_accel

		text_x-=text_speed
		text_speed+=text_accel


		if zoom_speed >= 0.0021400000000000047:
			done=True

		if text_x<=15:
			text_speed=0

		# print(text_x)



		clock.tick(30)


		pygame.display.flip()

# cutscene(screen,800,450,800,5,0.1)
running_game(screen)




