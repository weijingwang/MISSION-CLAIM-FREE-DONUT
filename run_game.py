import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

done = False

class player():
	"""docstring for player"""
	def __init__(self):
		self.image = pygame.Surface([100, 100])
		self.image.fill((255, 0, 0))

		self.rect = self.image.get_rect()


	def render(self):
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP]: self.rect[1] -= 3
		if pressed[pygame.K_DOWN]: self.rect[1] += 3
		if pressed[pygame.K_LEFT]: self.rect[0] -= 3
		if pressed[pygame.K_RIGHT]: self.rect[0] += 3
		# print(self.rect)
		screen.blit(self.image, self.rect)

class obstacle():
	"""docstring for obstacle"""
	def __init__(self):
		self.image = pygame.Surface([100, 100])
		self.image.fill((255, 0, 0))

		self.rect = self.image.get_rect()
		

	def render(self):
		self.rect[0] += 5
		if self.rect[0]>=1280:
			self.rect[0]=0-self.rect[2]
		# print(self.rect)
		screen.blit(self.image, self.rect)


me = player()
poop = obstacle()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill((0,0,0))
	me.render()
	poop.render()

	print(screen)
	pygame.display.flip()

# import pygame

# pygame.init()
# window = pygame.display.set_mode((250, 250))

# sprite1 = pygame.sprite.Sprite()
# sprite1.image = pygame.Surface((75, 75))
# sprite1.image.fill((255, 0, 0))
# sprite1.rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(75, 75)
# sprite2 = pygame.sprite.Sprite()
# sprite2.image = pygame.Surface((75, 75))
# sprite2.image.fill((0, 255, 0))
# sprite2.rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(75, 75)

# all_group = pygame.sprite.Group([sprite2, sprite1])
# test_group = pygame.sprite.Group(sprite2)

# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     sprite1.rect.center = pygame.mouse.get_pos()
#     collide = pygame.sprite.spritecollide(sprite1, test_group, False)

#     window.fill(0)
#     all_group.draw(window)
#     for s in collide:
#         pygame.draw.rect(window, (255, 255, 255), s.rect, 5, 1)
#     pygame.display.flip()

# pygame.quit()
# exit()