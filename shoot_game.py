import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1280, 720))



class target():
	"""docstring for target"""
	def __init__(self,x,y):
		self.x = x
		self.y = y

		self.width = 100
		self.height = 100
		self.color = (0, 128, 255)

		self.mouse_pos = pygame.mouse.get_pos()


	def draw_target(self):
		pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

	def turn_active(self):
		self.mouse_pos = pygame.mouse.get_pos()
		# print(self.mouse_pos)
		clicked = False
		if pygame.mouse.get_pressed()[0]:
			if self.mouse_pos[0] >= self.x and self.mouse_pos[0] <= self.x+self.width and self.mouse_pos[1] >= self.y and self.mouse_pos[1] <= self.y+self.height:
				self.color = (128,255,0)
				clicked = True
			else:
				self.color = (0, 128, 255)
				clicked = False

		else:
			self.color = (0, 128, 255)
			clicked = False
		return clicked



		#play color change of targets in order but dissapear
		#return the order so that it can be checked when player attempts to copy pattern
		pass
				
	def add_score(self):
		pass



def game(target_list,num_of_targets):
	#generate random order of targets and number of targets
	targets_this_game = []
	for x in range(num_of_targets):
		the_choice = random.choice(target_list)
		targets_this_game.append(the_choice)
		collide = the_choice.turn_active()
		if collide == True:
			print("YES")


	print(targets_this_game)

	return(targets_this_game)


done = False

one = target(100,100)
two = target(300,100)
three = target(500,100)
four = target(700,100)
five = target(100,300)
six = target(300,300)
seven = target(500,300)
eight = target(700,300)

all_targets = [one,two,three,four,five,six,seven,eight]

game(all_targets,3)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill((0,0,0))

	for x in all_targets:
		x.draw_target()
		x.turn_active()
	one.add_score()

	pygame.display.flip()
