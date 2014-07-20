import sys, pygame
pygame.init()

# CONSTANTS
WIDTH = 480
HEIGHT = 640
WHITE = 255, 255, 255
GUN_COORDS = 0, 320
KNIFE_COORDS = 100, 320
GRENADE_COORDS = 200, 320
DYNAMITE_COORDS = 300, 320

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

while 1:
#     # Player 1's Turn
     for event in pygame.event.get():
         if event.type == pygame.QUIT: sys.exit()
# 
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
