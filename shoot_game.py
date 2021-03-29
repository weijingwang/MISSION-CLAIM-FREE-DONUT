import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1280, 720))

shooting_range = pygame.image.load('shooting_range.png').convert_alpha()

class target():
	"""docstring for target"""
	def __init__(self,x,y):
		self.x = x
		self.y = y

		self.width = 200
		self.height = 200
		target = pygame.image.load('target.png').convert_alpha()
		self.image = target
		self.normal_color = (0, 128, 255)
		self.active_color = (128,255,0)

		self.color = self.normal_color

		self.mouse_pos = pygame.mouse.get_pos()

		self.active = False


	def draw_target(self,screen):
		pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
		screen.blit(self.image,(self.x,self.y))

	def turn_active(self,clicked):
		self.mouse_pos = pygame.mouse.get_pos()
		# print(self.mouse_pos)
		# print(clicked)

		if event.type == pygame.MOUSEBUTTONDOWN:

			if self.mouse_pos[0] >= self.x and self.mouse_pos[0] <= self.x+self.width and self.mouse_pos[1] >= self.y and self.mouse_pos[1] <= self.y+self.height:
				self.color = (128,255,0)


			else:
				self.color = (0, 128, 255)


		else:
			self.color = (0, 128, 255)


	def change_color(self,clicked):
		if clicked == True:
			print("ji")

		

				
	def add_score(self):
		pass



# def game(target_list,num_of_targets):
# 	#generate random order of targets and number of targets
# 	targets_this_game = []
# 	for x in range(num_of_targets):
# 		the_choice = random.choice(target_list)
# 		targets_this_game.append(the_choice)
# 		collide = the_choice.turn_active()
# 		if collide == True:
# 			print("YES")


# 	print(targets_this_game)

# 	return(targets_this_game)


done = False
clicked = False

one = target(90,100)
two = target(390,100)
three = target(690,100)
four = target(990,100)
five = target(90,400)
six = target(390,400)
seven = target(690,400)
eight = target(990,400)

all_targets = [one,two,three,four,five,six,seven,eight]

# game(all_targets,3)

button_color = ((0,100,20))

while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True



		else:
			clicked == False

	screen.blit(shooting_range,(0,0))

	for x in all_targets:
		x.draw_target(screen)
		check_button = x.turn_active(clicked)
		x.change_color(check_button)


	pygame.display.flip()
