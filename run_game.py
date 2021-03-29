import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1280, 720))

done = False


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
		self.rect.x = 200
		self.rect.y = 250

		# self.image.fill((255, 0, 0))

		self.speed_x=20


		self.floor = 250


		self.jump = False
		self.speed_y=17
		self.mass = 1


		self.shift = False

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
			if pressed[pygame.K_UP] or pressed[pygame.K_SPACE]:
				# print("jump")
				self.jump=True

		if self.jump==True:
			F =(1 / 2)*self.mass*(self.speed_y**2)

			self.rect[1]-= F

			self.speed_y -=2

			if self.speed_y<=0:

				self.mass = -1

			if self.speed_y <=-17:

				self.jump = False

				self.speed_y=17

				self.mass=1
				if collision==True:

					self.rect.y = 451-obstacle_height
					print(self.rect.y)
					
				else:
					self.rect.y = self.floor

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
		self.image = pygame.Surface([100, 200])
		self.image.fill((255, 0, 0))
		self.rect = self.image.get_rect()
		self.rect.x = 800
		self.rect.y = 450
		self.speed = 20

	def render(self,collision):

		if self.rect[0]<=0:
			self.rect[0]=1280-+self.rect[2]
		# print(self.rect)
		if collision ==True:
			# self.rect.x+=1
			self.speed = 0
			# print(self.rect[3])
			return self.rect[3]#height
		else:
			self.rect[0] -= 20
		screen.blit(self.image, self.rect)


class background():
	"""docstring for backgro"""
	def __init__(self, x,y):
		self.x=x
		self.y=y

		self.scroll_speed = 5
		self.image =pygame.image.load("background.png")

		self.meters_traveled = 0
		
	def draw(self,screen,collision):
		shake_speed = random.randrange(10)

		self.x-=self.scroll_speed
		self.meters_traveled+=self.scroll_speed/100



		print(self.meters_traveled)

		if self.x<=-1280:
			self.x=1280

		screen.blit(self.image,(self.x,self.y))


		displayText(screen,str("%.2f"%self.meters_traveled)+" meters",1000,25,60,255,0,0)

		if collision==True:
			self.scroll_speed=0

		else:
			self.scroll_speed =5



me = player()
poop = obstacle()

background_1 = background(0,0)
background_2 = background(1280,0)

clock = pygame.time.Clock()
collision = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True


	background_1.draw(screen,collision)
	background_2.draw(screen,collision)
	
	
	
	me.render(collision)

	me.update()

	obstacle_height = poop.render(collision)
	me.leap(collision,obstacle_height)
	me.crouch(collision)
	if me.rect.colliderect(poop.rect):

		collision = True
	else:
		collision = False

	# print(screen)
	# print(collision)
	clock.tick(30)

	pygame.display.flip()

