import pygame

pygame.init()

screen = pygame.display.set_mode((800, 450))

done = False

class player():
	"""docstring for player"""
	def __init__(self):
		self.image = pygame.Surface([100, 100])

		self.rect = self.image.get_rect()
		self.rect.x = 200
		self.rect.y = 200

		self.image.fill((255, 0, 0))

		self.speed_x=20


		self.floor = 350


		self.jump = False
		self.speed_y=10
		self.mass = 1

	def render(self,collision):
		pressed = pygame.key.get_pressed()
		# if pressed[pygame.K_UP]: self.rect[1] -= self.speed_y

		if pressed[pygame.K_LEFT]: self.rect[0] -= self.speed_x
		if pressed[pygame.K_RIGHT]: self.rect[0] += self.speed_x


		if collision ==True:
			# self.rect.x+=1
			self.speed_x = 0
		else:
			self.speed_x = 20

		# print(self.rect)
		screen.blit(self.image, self.rect)



	def leap(self):
		pressed = pygame.key.get_pressed()

		if self.jump==False:
			if pressed[pygame.K_SPACE]:
				print("jump")
				self.jump=True

		if self.jump==True:
			F =(1 / 2)*self.mass*(self.speed_y**2)

			self.rect[1]-= F

			self.speed_y -=2

			if self.speed_y<=0:

				self.mass = -1

			if self.speed_y <=-10:

				self.jump = False

				self.speed_y=10

				self.mass=1

				self.rect.y = 200







class obstacle():
	"""docstring for obstacle"""
	def __init__(self):
		self.image = pygame.Surface([100, 100])
		self.image.fill((255, 0, 0))
		self.rect = self.image.get_rect()
		self.rect.x = 300
		self.rect.y = 300
		self.speed = 20

	def render(self,collision):

		if self.rect[0]<=0:
			self.rect[0]=1280-+self.rect[2]
		# print(self.rect)
		if collision ==True:
			# self.rect.x+=1
			self.speed = 0
		else:
			self.rect[0] -= 20
		screen.blit(self.image, self.rect)


me = player()
poop = obstacle()
clock = pygame.time.Clock()
collision = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True


	screen.fill((0,0,0))
	me.render(collision)
	poop.render(collision)
	me.leap()
	if me.rect.colliderect(poop.rect):

		collision = True
	else:
		collision = False

	# print(screen)
	# print(collision)
	clock.tick(30)

	pygame.display.flip()

