import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))



class thing():
	"""docstring for thing"""
	def __init__(self, z, width, height):
		self.z = z
		self.width = width
		self.height = height

	def draw_thing(self,player_z):
		distance = self.z - player_z
		visual_width = (1/distance)*(self.width)
		visual_height = (1/distance)*(self.height)

		pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(500, 100, visual_width, visual_height))
		pygame.display.flip()

		


done = False
player_z = 0


test_thing = thing(100,4000,9000)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]: player_z +=0.3
	if pressed[pygame.K_DOWN]: player_z -=0.3

	#test thing







	screen.fill((0,0,0))



	test_thing.draw_thing(player_z)

	print(player_z)

	pygame.display.flip()



