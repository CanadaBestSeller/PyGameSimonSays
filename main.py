import sys, pygame
pygame.init()

# CONSTANTS
WIDTH = 480
HEIGHT = 500
WHITE = 255, 255, 255
GUN_COORDS = WIDTH*0.1, (HEIGHT-64)/2
KNIFE_COORDS = WIDTH*0.3, (HEIGHT-64)/2
GRENADE_COORDS = WIDTH*0.5, (HEIGHT-64)/2
DYNAMITE_COORDS = WIDTH*0.7, (HEIGHT-64)/2

#CUSTOMIZATIONS
SIZE = WIDTH, HEIGHT
BACKGROUND_COLOR = WHITE

gun = pygame.image.load("gun.bmp")
knife = pygame.image.load("knife.bmp")
grenade = pygame.image.load("grenade.bmp")
dynamite = pygame.image.load("dynamite.bmp")
rect = gun.get_rect()

button_tuples = [(gun, (GUN_COORDS)),
                 (knife, (KNIFE_COORDS)),
                 (grenade, (GRENADE_COORDS)),
                 (dynamite, (DYNAMITE_COORDS))]

# INITIALIZATION
screen = pygame.display.set_mode(SIZE)
screen.fill(BACKGROUND_COLOR)
for b in button_tuples:
    screen.blit(b[0], b[1])
pygame.display.flip()
player1_pattern = []
player2_pattern = []
set_number = 1;

while 1:
	## Player 1's Turn

	# Player 1 Records
     for event in pygame.event.get():
         if event.type == pygame.QUIT: sys.exit()
         while pressed_count < set_number:
 	        if player_count < button_count:
		        last_tur = false
		        if event.type == pygame.MOUSEBUTTONDOWN:
    	  	   	x, y = event.pos
        	 	if x > GUN_COORDS[0] and x < GUN_COORDS[0] + 64 and
         			y > GUN_COORDS[1] and y < GUN_COORDS[1] + 64:
         			player1_pattern = player1_pattern.append("gun")
         			player_count += 1

         		if x > KNIFE_COORDS[0] and x < KNIFE_COORDS[0] + 64 and
         			y > KNIFE_COORDS[1] and y < KNIFE_COORDS[1] + 64:
         			player1_pattern = player1_pattern.append("knife")
     				player_count += 1


         		if x > GRENADE_COORDS[0] and x < GRENADE_COORDS[0] + 64 and
         			y > GRENADE_COORDS[1] and y < GRENADE_COORDS[1] + 64:
         			player1_pattern = player1_pattern.append("knife")
         			player_count += 1

         		if x > DYNAMIE_COORDS[0] and x < DYNAMIE_COORDS[0] + 64 and
         			y > DYNAMIE_COORDS[1] and y < DYNAMIE_COORDS[1] + 64:
         			player1_pattern = player1_pattern.append("knife")
         			player_count += 1



#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]
# 
#     screen.fill(white)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()
# 
#     # Player 1's Turn
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
# 
#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]
