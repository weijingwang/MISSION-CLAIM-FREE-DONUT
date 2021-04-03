import pygame
import random
pygame.mixer.pre_init()
pygame.init()
pygame.display.set_caption("MISSION: CLAIM FREE DONUT (pyweek 31)")

class player():
	"""docstring for player"""
	def __init__(self):
		# self.image = pygame.Surface([100, 400])

		#images

		self.images = []
		self.imagesR = []
		self.imagesR.append(pygame.image.load('./assets/player-1.png').convert_alpha())
		self.imagesR.append(pygame.image.load('./assets/player-1.png').convert_alpha())
		self.imagesR.append(pygame.image.load('./assets/player-2.png').convert_alpha())
		self.imagesR.append(pygame.image.load('./assets/player-3.png').convert_alpha())
		self.imagesR.append(pygame.image.load('./assets/player-4.png').convert_alpha())
		self.imagesR.append(pygame.image.load('./assets/player-4.png').convert_alpha())
		self.imagesR.append(pygame.image.load('./assets/player-3.png').convert_alpha())
		self.imagesR.append(pygame.image.load('./assets/player-2.png').convert_alpha())

		self.imagesL = []
		self.imagesL.append(pygame.transform.flip(pygame.image.load('./assets/player-1.png').convert_alpha(), True, False))
		self.imagesL.append(pygame.transform.flip(pygame.image.load('./assets/player-1.png').convert_alpha(), True, False))
		self.imagesL.append(pygame.transform.flip(pygame.image.load('./assets/player-2.png').convert_alpha(), True, False))
		self.imagesL.append(pygame.transform.flip(pygame.image.load('./assets/player-3.png').convert_alpha(), True, False))
		self.imagesL.append(pygame.transform.flip(pygame.image.load('./assets/player-4.png').convert_alpha(), True, False))
		self.imagesL.append(pygame.transform.flip(pygame.image.load('./assets/player-4.png').convert_alpha(), True, False))
		self.imagesL.append(pygame.transform.flip(pygame.image.load('./assets/player-3.png').convert_alpha(), True, False))
		self.imagesL.append(pygame.transform.flip(pygame.image.load('./assets/player-2.png').convert_alpha(), True, False))

		self.images = self.imagesR
		self.facing_right = True



		self.index = 0
		self.image = self.images[self.index]

		self.rect = self.image.get_rect()
		self.rect.x = 200
		self.rect.y = 402

		# self.image.fill((255, 0, 0))

		self.speed_x=20


		self.floor = 402


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
		elif self.rect[0]<=0:
			self.rect[0] = 0
			self.rect[0]+=10
		else:
			if pressed[pygame.K_LEFT]:
				self.rect[0] -= self.speed_x
				self.facing_right = False
			if pressed[pygame.K_RIGHT]:
				self.rect[0] += self.speed_x
				self.facing_right = True

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
		if self.facing_right == True:
			self.images = self.imagesR
		elif self.facing_right == False:
			self.images = self.imagesL

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

		# print(ready_jump)

		# print(str(self.power))

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
	def __init__(self,is_cutscene):

		self.image = pygame.image.load('./assets/apple.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = 1280
		self.rect.y = 450
		self.speed = 20

		
		self.images = []
		self.images.append(pygame.image.load('./assets/police-d1.png').convert_alpha())
		self.images.append(pygame.image.load('./assets/police-d2.png').convert_alpha())
		self.index = 0
		if is_cutscene==True:
			self.image = self.images[self.index]
			self.rect.y = 250


		self.is_cutscene = is_cutscene
		if self.is_cutscene == True:
			self.rect.x = 1400

	def render(self,collision,is_stopped):

		if self.rect[0]<=0:
			self.rect[0]=1280-+self.rect[2]
		# print(self.rect)
		if collision ==True:
			# self.rect.x+=1
			self.speed = 0
			# print(self.rect[3])
			return self.rect[3]#height
		elif is_stopped == True:
			self.speed = 0
		else:
			self.rect[0] -= 20
		screen.blit(self.image, self.rect)

	def update(self):
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]

class background():
	"""docstring for backgro"""
	def __init__(self, x,y,scroll_speed,image,score_counter,is_cutscene,stop_after):
		self.x=x
		self.y=y
		self.scroll_speed = scroll_speed
		self.image =pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.meters_traveled = 0
		self.scroll_speed_bank = scroll_speed

		self.score_counter = score_counter
		self.is_cutscene = is_cutscene
		self.stop_after = stop_after
		self.is_stopped = False

		
	def draw(self,screen,collision):

		self.x-=self.scroll_speed

		if self.x<=-1280:
			self.x=1280

		screen.blit(pygame.transform.scale(self.image,(1280,720)),(self.x,self.y))

		# screen.blit(pygame.transform.scale(blackTexture, (800, 600)), (0, 0))

		if collision==True:
			self.scroll_speed=0

		elif self.is_cutscene ==True and self.meters_traveled >=self.stop_after:
			self.scroll_speed=0
			self.is_stopped = True

		else:
			self.scroll_speed =self.scroll_speed_bank

		# print(self.meters_traveled)
		if self.score_counter == True:
			displayText(screen,str("%.2f"%self.meters_traveled)+" meters",1000,25,60,255,0,0)
			self.meters_traveled+=self.scroll_speed/100
			if self.is_cutscene == False:
				displayText(screen,"/100 meters",1000,75,30,255,0,0)
			return self.meters_traveled

	def return_stop(self):
		return self.is_stopped

class police():
	"""docstring for police"""
	def __init__(self,word_list,cutscene):

		self.speed = 2
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
		self.previous_word = ""

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


		self.police_icon = pygame.image.load('./assets/police-p.png').convert_alpha()

		self.cutscene = cutscene

		self.skip = False

	def txt_game(self,event):
		# print(self.previous_word+" "+self.word)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				self.output = self.text
				self.text = ""

				if self.output==self.word:
					self.points +=1
					if self.cutscene == True:
						# print("police works")
						return True

					self.previous_word = self.word
					if self.rect[0] >-100:
						self.word = random.choice(self.word_list)
						# print("next")
						self.attack = True
						self.txt_cooldown = 0
					# if police_finished_move == True:
					# 	self.hit = False
					# 	print(self.hit)
					# else:
					# 	self.hit= True
					# 	print(self.hit)

				elif self.output == "skip":
					self.skip = True
					return self.skip

			elif event.key == pygame.K_BACKSPACE:
				self.text = self.text[:-1]
			else:
				self.text += event.unicode

		if self.word == self.previous_word:
			# print("warn")
			self.word = random.choice(self.word_list)


	def txt_draw(self):
		# print(self.cutscene)		
		if self.cutscene == True:
			# print("hi")		
			self.txt_rect1 = self.txt_surface1.get_rect()
			self.txt_surface1 = self.font.render(self.word, True, self.red)
			screen.blit(self.txt_surface1, ((1280/2)-self.txt_rect1[2]/2, 600))

			self.txt_rect = self.txt_surface.get_rect()
			self.txt_surface = self.font.render(self.text, True, self.color)
			screen.blit(self.txt_surface, ((1280/2)-self.txt_rect[2]/2, 600))
				
		else:
			if self.rect[0]>-200:
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
			self.rect[0]-=165
			self.attack=False
		else:
			if collision==True:
				self.rect[0]+=self.speed + 2
			if collision==False:
				self.rect[0]+= self.speed
		if self.rect[0]<0:
			screen.blit(self.police_icon, (0,0))


		screen.blit(self.image, self.rect)

	def update(self):
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]

class story_game():
	"""docstring for interactive_text"""
	def __init__(self,text,images):
		self.count_text = 0
		self.index = 0
		# self.count_image = 0

		self.font_S = pygame.font.Font(None, 60)
		self.font = pygame.font.Font(None, 80)
		self.color = (255,255,255)

		self.text = text
		self.current_text = self.text[self.count_text][1]
		self.current_text_S = self.text[self.count_text][0]
		self.txt_surface = self.font.render(self.current_text, True, self.color)
		self.txt_surface_S = self.font.render(self.current_text_S, True, self.color)
		self.txt_rect = self.txt_surface.get_rect()
		self.txt_rect_S = self.txt_surface_S.get_rect()
		self.txt_x = self.txt_rect[2]#
		self.txt_x_S = self.txt_rect_S[2]#
		

		self.backTexture = pygame.image.load("./assets/backTexture.png").convert_alpha()

		self.finished = False

		self.next_scene = False

		self.images = images
		self.image = self.images[self.count_text]
		self.current_image = self.image[self.index]

		self.timer_text = 0
		# self.timer_images = 0
		self.clock = pygame.time.Clock()

		self.time_text = self.text[self.count_text][2] *15
		# self.time_images =self.images[self.count_image][1]*30

		

	def render_text(self,screen):
		self.image = self.images[self.count_text]
		self.current_image = self.image[self.index]		


		self.time_text = self.text[self.count_text][2] *15
		self.current_text = self.text[self.count_text][1]
		self.current_text_S = self.text[self.count_text][0]
		self.image = self.images[self.count_text]
		
		self.txt_rect = self.txt_surface.get_rect()
		self.txt_rect_S = self.txt_surface_S.get_rect()
		self.txt_surface = self.font.render(self.current_text, True, self.color)
		self.txt_surface_S = self.font_S.render(self.current_text_S, True, self.color)

		screen.blit(self.current_image,(0,0))
		screen.blit(pygame.transform.scale(self.backTexture, (1280, 150)), (0, 570))
		# print(self.count_text,self.current_text,self.image)
		screen.blit(self.txt_surface_S, (100, 580))#(1280/2)-self.txt_rect[2]/2
		screen.blit(self.txt_surface, (50, 640))

		# print(self.time_text)


		self.timer_text+=1

		if self.timer_text >= self.time_text:
			self.next_scene = True
			self.timer_text = 0
		else:
			self.next_scene = False

		self.clock.tick(15)


		pygame.display.flip()

	def update(self):
		# print(self.current_image)
		self.index += 1
		if self.index >= len(self.image):
			self.index = 0
		self.current_image = self.image[self.index]


	def detect_next(self):

		if self.next_scene == True:
			if (self.count_text+1) == len(self.text):
				self.count_text = self.count_text
				self.finished = True
			# print(self.finished)
			if self.finished == False:
				self.count_text +=1
				self.current_text = self.text[self.count_text]
			elif self.finished==True:
				self.count_text = self.count_text
				self.finished = True
		return self.finished

def title_screen(screen,width,height,text_x,text_speed,text_accel,text_x2,text_speed2,song,background,image1, image2):
	pygame.mixer.music.load(song)
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
				if event.key == pygame.K_SPACE:
					done= True

		x=((1280/2)-(width/2))		
		y=((720/2)-(height/2))

		screen.blit(pygame.transform.scale(background,(width,height)),(x,y))
		screen.blit(image1,(text_x,30))#380
		screen.blit(image2,(text_x2,620))#380

		width+=int(width*zoom_speed)
		height+=int(height*zoom_speed)

		zoom_speed+=zoom_accel

		text_x-=text_speed
		text_x2-=text_speed2
		text_speed+=text_accel


		if zoom_speed >= 0.0021400000000000047:
			zoom_speed =0

		if text_x<=15:
			text_speed=0
		if text_x2<=0:#544
			text_speed2=0

		# print(text_x)
		clock.tick(30)


		pygame.display.flip()

def running_game(screen):
	me = player()
	poop = obstacle(False)
	chasers = police(word_list,False)
	# background_1 = background(0,0,5)
	# background_2 = background(1280,0,5)

	city_back1a = background(0,0,5,"./assets/city_back1.png",False,False,20)
	player_meters_traveled = city_back1b = background(1280,0,5,"./assets/city_back1.png",True,False,20)

	city_back2a = background(0,0,1,"./assets/city_back2.png",False,False,20)
	city_back2b = background(1280,0,1,"./assets/city_back2.png",False,False,20)
	grass = background(0,0,20,"./assets/grass.png",False,False,20)
	grassb = background(1280,0,20,"./assets/grass.png",False,False,20)

	clock = pygame.time.Clock()

	done = False
	collision = False

	get_caught = False
	finish_game = False

	win = None
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			finish_game = chasers.txt_game(event)

		# background_1.draw(screen,collision)
		#  background_2.draw(screen,collision)
		
		screen.fill((130,206,235))

		city_back2a.draw(screen,collision)
		city_back2b.draw(screen,collision)

		city_back1a.draw(screen,collision)
		player_meters_traveled =city_back1b.draw(screen,collision)

		grass.draw(screen,collision)
		grassb.draw(screen,collision)
		
		me.render(collision)

		me.update()

		obstacle_height = poop.render(collision,False)
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
			win = False
			return win
		else:
			get_caught = False


		if player_meters_traveled >= 100:
			# print("win")
			win = True
			pygame.mixer.fadeout(1000)# does this work??????
			return win	

		if finish_game == True:
			# print("skipped")
			done = True
		# print(screen)
		# print(collision)
		clock.tick(30)

		pygame.display.flip()

def steal_donut(screen):
	me = player()
	donut = obstacle(True)
	city_back1a = background(0,0,5,"./assets/city_back1.png",True,True,2)
	player_meters_traveled = city_back1b = background(1280,0,5,"./assets/city_back1.png",True,True,2)
	text_only = police(["steal donut"],True)

	clock = pygame.time.Clock()
	done = False
	finish_game = False
	collision = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			finish_game = text_only.txt_game(event)

		screen.fill((130,206,235))

		city_back1a.draw(screen,collision)
		player_meters_traveled =city_back1b.draw(screen,collision)
		stopped = city_back1b.return_stop()
		me.render(collision)
		me.update()
		obstacle_height = donut.render(collision,stopped)
		donut.update()
		me.leap(collision,obstacle_height)
		me.power_bar(screen)

		screen.blit(instructions,(0,0))

		text_only.txt_draw()
		

		if me.rect.colliderect(donut.rect):

			collision = True
		else:
			collision = False

		# print(finish_game)
		if finish_game == True:
			# print("skipped")
			done = True
		clock.tick(30)

		pygame.display.flip()

def lose_event(screen,image,image2):
	pygame.mixer.music.load("./assets/music/lose.mp3")
	pygame.mixer.music.play(-1,0.0)
	done = False
	clock = pygame.time.Clock()
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					done= True
		random_num1 = random.randrange(-2,2)
		random_num2 = random.randrange(-2,2)
		screen.blit(image,(0,0))
		screen.blit(image2,(0+random_num1,676+random_num2))
		clock.tick(30)
		pygame.display.flip()

def intro(screen):
	pygame.mixer.music.load("./assets/music/police_music.mp3")
	pygame.mixer.music.play(-1,0.0)
	scene1 = pygame.image.load("./assets/scene1.png").convert_alpha()
	scene2 = pygame.image.load("./assets/scene2.png").convert_alpha()
	scene3 = pygame.image.load("./assets/scene3.png").convert_alpha()

	scene = scene1

	done = False
	clock = pygame.time.Clock()
	timer = 0
	count = 0
	alphaSurface = pygame.Surface((1280,720)) # The custom-surface of the size of the screen.
	alphaSurface.fill((0,0,0))
	alphaSurface.set_alpha(0) # Set alpha to 0 before the main-loop. 
	alph = 0 # The increment-variable.
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					done= True

		screen.blit(scene,(0,0))


		if timer>=0:
			scene = scene1
			if timer >=6:
				scene=scene2
				if timer>=24:
					scene = scene3
					if timer>=36:
						alph += 20
						if alph >= 480:
							done=True

		timer +=1

		
		alphaSurface.set_alpha(alph)
		screen.blit(alphaSurface,(0,0))
		# print(timer,count)
		clock.tick(12)
		pygame.display.flip()

def displayText(surface,message,x,y,size,r,g,b):
	myfont = pygame.font.Font(None,size)
	textImage = myfont.render(message, True, (r,g,b))
	surface.blit(textImage,(x,y))
		
def ending(screen,words,images):
	done = False
	clock = pygame.time.Clock()
	game_done = False
	test_text = story_game(words,images)
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			

		screen.fill((0,0,0))
		# pygame.draw.rect(screen,(100,100,100),(0,570,1280,150))
		game_done = test_text.detect_next()
		test_text.render_text(screen)
		test_text.update()

		if game_done==True:
			done = True

screen = pygame.display.set_mode((1280, 720))

title = pygame.image.load("./assets/title.png").convert_alpha()
title_text1 = pygame.image.load("./assets/mission.png").convert_alpha()
titletext2 = pygame.image.load("./assets/accept.png").convert_alpha()
lose = pygame.image.load("./assets/lose.jpg").convert_alpha()
fail = pygame.image.load("./assets/mission_fail.png").convert_alpha()
instructions = pygame.image.load("./assets/instructions.png").convert_alpha()
scene4 = pygame.image.load("./assets/scene4.png").convert_alpha()
scene5 = pygame.image.load("./assets/scene5.png").convert_alpha()
scene6 = pygame.image.load("./assets/scene6.png").convert_alpha()
scene7 = pygame.image.load("./assets/scene7.png").convert_alpha()
scene8 = pygame.image.load("./assets/scene8.png").convert_alpha()
scene9 = pygame.image.load("./assets/scene9.png").convert_alpha()
scene10 = pygame.image.load("./assets/scene10.png").convert_alpha()
scene10_grey = pygame.image.load("./assets/scene10_grey.png").convert_alpha()
win = pygame.image.load("./assets/win.png").convert_alpha()
thanks = pygame.image.load("./assets/thanks.png").convert_alpha()

word_list = ["pizza pie","hey guys","taco tuesday","samosa","scallion","boss","pov","mfw when","apple","banana","orange","grape","ringo","dog","bark","dance cat","pants","boil","eel",
"smh my head","police","water","rojo","please","fast","donut","frog","baby","music","car","chase","money","gambling","kid",
"dance","goat","runner","prank","consume"
]

ending_text = [["","",4],["cop","*gasp heh u are a quick one... kid *huff huff",5],["kid","mmm this is one tasty donut",4],["kid","*aggressively munches on donut",3],["cop",".............",2],["kid","*wolfs down donut and scratches chin",4],["","MISSION ACCOMPLISHED",3]]
ending_images = [[scene4,scene4],[scene5,scene5],[scene6,scene6],[scene7,scene8],[scene7,scene8],[scene9,scene9],[scene10,scene10]]

title_screen(screen,1280,720,1280,5,0.1,2000,10,"./assets/music/national_anthem.mp3",title,title_text1,titletext2)#song,background,image1, image2
steal_donut(screen)
intro(screen)
result = running_game(screen)
if result == True:
	print("YOU WIN")
	ending(screen,ending_text,ending_images)
	title_screen(screen,1280,720,1280,5,0.1,2000,10,"./assets//music/MISSION_ACCOMPLISHED.mp3",scene10_grey,thanks,win)#song,background,image1, image2
elif result == False:
	print("LOSE")
	lose_event(screen,lose, fail)


