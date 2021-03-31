import pygame
import random
pygame.mixer.pre_init()

pygame.init()

screen = pygame.display.set_mode((1280, 720))


word_list = ["pizza pie","hey guys","taco tuesday","samosa","scallion","boss","pov","mfw when","apple","banana","orange","grape","ringo","dog","cat","pants","boil","eel"]


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
		self.images.append(pygame.image.load('./assets/player-1.png').convert_alpha())
		self.images.append(pygame.image.load('./assets/layer-2.png').convert_alpha())
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

		self.power = 100
		self.power_max=100
		self.ready_jump = True

		self.active_color = (0,255,255)

	def render(self,collision):
		pressed = pygame.key.get_pressed()
		# if pressed[pygame.K_UP]: self.rect[1] -= self.speed_y



		if self.rect[0]>=1200:
			self.rect[0] = 1200
			self.rect[0]-=50
		else:
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
			self.power+=5
			if self.power >= self.power_max:
				self.power = self.power_max
			if self.power <= 0:
				self.power = 0
				# print("set to 0")

			if pressed[pygame.K_UP] and self.power==100:
				# print("jump")
				self.power-=100

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
					# print(self.rect.y)
					
				else:
					self.rect.y = self.floor

		if self.power < 100:
			ready_jump = False
		elif self.power >= 100:
			ready_jump = True

		print(ready_jump)

		print(str(self.power))

		# print(self.power)
	def power_bar(self,screen):
		if self.power >= 100:
			self.active_color = (0,255,255)
		else:
			self.active_color = (0,255,0)

		pygame.draw.rect(screen, (255,0,0), pygame.Rect(50, 25, 500, 5))
		pygame.draw.rect(screen, self.active_color, pygame.Rect(50, 25, 500*(self.power/100), 5))



class obstacle():
	"""docstring for obstacle"""
	def __init__(self):

		self.image = pygame.image.load('./assets/apple.png').convert_alpha()
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
	def __init__(self, x,y,scroll_speed,image,score_counter):





		self.x=x
		self.y=y
		self.scroll_speed = scroll_speed
		self.image =pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.meters_traveled = 0
		self.scroll_speed_bank = scroll_speed

		self.score_counter = score_counter
		
	def draw(self,screen,collision):

		self.x-=self.scroll_speed

		if self.x<=-1280:
			self.x=1280

		screen.blit(pygame.transform.scale(self.image,(1280,720)),(self.x,self.y))

		# screen.blit(pygame.transform.scale(blackTexture, (800, 600)), (0, 0))



		if collision==True:
			self.scroll_speed=0

		else:
			self.scroll_speed =self.scroll_speed_bank

		# print(self.meters_traveled)
		if self.score_counter == True:
			displayText(screen,str("%.2f"%self.meters_traveled)+" meters",1000,25,60,255,0,0)
			self.meters_traveled+=self.scroll_speed/100
			return self.meters_traveled

class police():
	"""docstring for police"""
	def __init__(self,word_list):

		self.speed = 1
		self.meters_traveled = -5

		self.images = []
		self.images.append(pygame.image.load('./assets/police-1.png').convert_alpha())
		self.images.append(pygame.image.load('./assets/police-2.png').convert_alpha())
		self.index = 0
		self.image = self.images[self.index]

		self.rect = self.image.get_rect()
		self.rect.x = -200
		self.rect.y = 250

		self.xchange = 0

		self.finish_move = True
		self.move_distance =0


		self.font = pygame.font.Font(None, 80)

		self.aqua = pygame.Color(56,254,220)
		self.red = pygame.Color(255,0,0)

		self.color = self.aqua
		self.text = ""
		self.txt_surface = self.font.render(self.text, True, self.color)
		self.txt_rect = self.txt_surface.get_rect()
		self.txt_x = self.txt_rect[2]#
		self.txt_length = 0

		self.word_list = word_list
		self.word = random.choice(self.word_list)

		self.output = ""
		self.output_store = ""

		self.points = 0

		self.attack = False


		self.txt_surface1 = self.font.render(self.text, True, self.color)
		self.txt_rect1 = self.txt_surface.get_rect()
		self.txt_x1 = self.txt_rect[2]#
		self.txt_length1 = 0

		self.txt_cooldown = 100
		self.next_word = True



	def txt_game(self,event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				self.output = self.text
				self.text = ""

				if self.output==self.word:
					self.points +=1
					
					if self.txt_cooldown==100:
						self.word = random.choice(self.word_list)
						print("next")

						self.attack = True
						self.txt_cooldown = 0
					# if police_finished_move == True:
					# 	self.hit = False
					# 	print(self.hit)
					# else:
					# 	self.hit= True
					# 	print(self.hit)

			elif event.key == pygame.K_BACKSPACE:
				self.text = self.text[:-1]
			else:
				self.text += event.unicode

		if self.txt_cooldown <100:
			self.txt_cooldown+=5
			self.next_word = False
		elif self.txt_cooldown >=100:
			self.txt_cooldown = 100
			self.next_word = True


	def txt_draw(self):
		self.txt_rect1 = self.txt_surface1.get_rect()
		self.txt_surface1 = self.font.render(self.word, True, self.red)
		screen.blit(self.txt_surface1, ((1280/2)-self.txt_rect1[2]/2, 600))

		self.txt_rect = self.txt_surface.get_rect()
		self.txt_surface = self.font.render(self.text, True, self.color)
		screen.blit(self.txt_surface, ((1280/2)-self.txt_rect[2]/2, 600))

	def chase(self,collision):
		# self.meters_traveled+=self.speed/100
		# print(self.meters_traveled)
			# self.finish_move = True
		if self.attack ==True:
			self.rect[0]-=150
			self.attack=False
		else:
			if collision==True:
				self.rect[0]+=self.speed + 5
			if collision==False:
				self.rect[0]+= self.speed
				# print(self.rect[0])
			# print(collision)
			# print(self.rect[0])
			
			# if self.meters_traveled>=player_meters_traveled:
			# 	print("lose")


		screen.blit(self.image, self.rect)

	def update(self):
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]


		






def running_game(screen):

	me = player()
	poop = obstacle()
	chasers = police(word_list)
	# background_1 = background(0,0,5)
	# background_2 = background(1280,0,5)

	city_back1a = background(0,0,5,"./assets/city_back1.png",False)
	player_meters_traveled = city_back1b = background(1280,0,5,"./assets/city_back1.png",True)

	city_back2a = background(0,0,1,"./assets/city_back2.png",False)
	city_back2b = background(1280,0,1,"./assets/city_back2.png",False)
	grass = background(0,0,20,"./assets/grass.png",False)
	grassb = background(1280,0,20,"./assets/grass.png",False)


	clock = pygame.time.Clock()

	done = False
	collision = False

	get_caught = False

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			chasers.txt_game(event)

		# background_1.draw(screen,collision)
		#  background_2.draw(screen,collision)
		
		screen.fill((50,50,50))

		city_back2a.draw(screen,collision)
		city_back2b.draw(screen,collision)

		city_back1a.draw(screen,collision)
		player_meters_traveled =city_back1b.draw(screen,collision)

		grass.draw(screen,collision)
		grassb.draw(screen,collision)
		
		me.render(collision)

		me.update()

		obstacle_height = poop.render(collision)
		me.leap(collision,obstacle_height)

		chasers.chase(collision)
		chasers.update()

		chasers.txt_draw()
		# print(hit_police)

		me.power_bar(screen)


		if me.rect.colliderect(poop.rect):

			collision = True
		else:
			collision = False

		if me.rect.colliderect(chasers.rect):
			get_caught = True
			quit()		
		else:
			get_caught = False


		if player_meters_traveled >= 100:
			print("win")
			done = True

		# print(screen)
		# print(collision)
		clock.tick(30)

		pygame.display.flip()

# class cutscene():
# 	"""docstring for cutscene"""
# 	def __init__(self):
# 		self.arg = arg
		





cutscene_1 = pygame.image.load("./assets/cutscene_1.png").convert_alpha()
cutscene_1text = pygame.image.load("./assets/cutscene_1b.png").convert_alpha()
cutscene_2 = pygame.image.load("./assets/cutscene_2.png").convert_alpha()
cutscene_3 = pygame.image.load("./assets/cutscene_3.png").convert_alpha()

width = 1280
height = 720

text_x = 1280
text_speed = 5
text_accel = 0.1
def cutscene(screen,width,height,text_x,text_speed,text_accel):
	pygame.mixer.music.load("./assets/national_anthem.mp3")
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
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					done= True

		x=((1280/2)-(width/2))		
		y=((720/2)-(height/2))




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

cutscene(screen,1280,720,1280,5,0.1)
running_game(screen)
