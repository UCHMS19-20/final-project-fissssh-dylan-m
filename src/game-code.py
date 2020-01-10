# import pygame module in this program 
import pygame 
import time
import random
  
# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 

# define the RGB value 
# for white colour 
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
  
# assigning values to X and Y variable 
X = 698
Y = 340
  
# create the display surface object 
# of specific dimension..e(X, Y).
pygame.display.set_mode((X, Y ))
display_surface = pygame.display.set_mode((X, Y )) 


# set the pygame window name 
pygame.display.set_caption('Fishing Simulator') 
  
# create a surface object, image is drawn on it. 
image = pygame.image.load(r'C:\Users\dmccann\Documents\Final Project Babyy\final-project-fissssh-dylan-m\src\img\Test_Opening.png') 
image2 = pygame.image.load(r'C:\Users\dmccann\Documents\Final Project Babyy\final-project-fissssh-dylan-m\src\img\FishingMan.jpg')
fish1 = pygame.image.load(r'C:\Users\dmccann\Documents\Final Project Babyy\final-project-fissssh-dylan-m\src\img\Fish1.png')
Fish1_Small = pygame.transform.scale(fish1, (50, 50))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    gameDisplay.blit(fish1,(x,y))


done = False
intro_page = 1
display_intro = True

class fish(object):
    

    def __init__(self,x,y,width,height,end):
        self.x = random.randint(0, display_width)
        self.y = random.randint(0, display_height)
        self.width = width
        self.height = height
        self.end= end
                
while not done and display_intro:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            intro_page += 1  
        if intro_page == 2:
                display_intro = False  
    if intro_page == 1:
         # completely fill the surface object 
         # with white colour 
         display_surface.fill(white) 
         
         # copying the image surface object 
         # to the display surface object at (0, 0) coordinate. 
         display_surface.blit(image, (0, 0)) 
         pygame.display.update()

enemies = []
fish1_event = pygame.USEREVENT + 1
x = random.randint(3000,6000)
pygame.time.set_timer(fish1_event, x)
fishreact = 1000
 

# infinite loop 
while True : 
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method.
    clock= pygame.time.Clock()   
    display_surface = pygame.display.set_mode((1000, 670 ))
    display_surface.blit(image2, (0, 0))
    print(event)
    for event in pygame.event.get() : 
        # Spawn enemies if counter <= 0 then reset it.
        if event.type == fish1_event:
            enemies.append(Fish1_Small.get_rect(topleft=(random.randrange(600), 400)))
            if event.type == pygame.K_SPACE in fishreact:
                pygame.quit() 
                sys.exit()
            # else:
            #     fish dissappears and more fish can spawn again
              
        for enemy_rect in enemies:
            display_surface.blit(Fish1_Small, enemy_rect)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
        

        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
  
            # deactivates the pygame library 
            pygame.quit() 
  
            # quit the program. 
            quit() 
  
        # Draws the surface object to the screen. 
