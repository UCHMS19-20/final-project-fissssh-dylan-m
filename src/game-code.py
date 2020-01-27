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
display_surface = pygame.display.set_mode((X, Y )) 

#time
clock = pygame.time.Clock()   

# set the pygame window name 
pygame.display.set_caption('Fishing Simulator') 
  
# setting images and sizes of those images
image = pygame.image.load(r'src\img\Test_Opening.png') 
image2 = pygame.image.load(r'src\img\FishingMan.jpg')
fish1 = pygame.image.load(r'src\img\Fish1.png')
fish2 = pygame.image.load(r'src\img\Fish2.png')
nice = pygame.image.load(r'src\img\nice-catch.jpg')
fail = pygame.image.load(r'src\img\Fail.jpg')
fail_small = pygame.transform.scale(fail, (100, 100))
Fish1_Small = pygame.transform.scale(fish1, (50, 50))
Fish2_Small = pygame.transform.scale(fish2, (50, 50))

done = False
intro_page = 1

class Fish:
    def __init__(self, time, clicks):
        self.t = time
        self.c = clicks

x = random.randint(3000,6000)
y = random.randint(7000,11000)
blue = Fish(x, 10)    
red = Fish(y, 20)    


while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            pygame.quit() 
            quit()
            # Quit the program
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:# If user clicked space
            done = True
            #leave the intro page and go to the main game loop          
    if intro_page == 1:
         # completely fill the surface object 
         # with white colour 
         display_surface.fill(white) 
         
         # copying the image surface object 
         # to the display surface object at (0, 0) coordinate. 
         display_surface.blit(image, (0, 0)) 
         pygame.display.update()

enemies = []
catches = 0
bro = 0
fish1_event = pygame.USEREVENT + 1
a = 1

pygame.time.set_timer(fish1_event, blue.t)


# infinite loop 
while True : 
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method.
    display_surface = pygame.display.set_mode((1000, 670 ))
    display_surface.blit(image2, (0, 0))
    
    for event in pygame.event.get(): 
        
        pressed = pygame.key.get_pressed()
        
        if event.type == fish1_event:
            if random.choice([0,3]) != 0:
                bruh = Fish1_Small.get_rect(topleft=(random.randrange(600), 400))
                cool = Fish1_Small
                a = 1
            else: 
                bruh = Fish2_Small.get_rect(topleft=(random.randrange(600), 400))
                cool = Fish2_Small
                a = 5
            enemies.append(bruh)
            print(enemies)
        if pressed[pygame.K_SPACE] and len(enemies) >= 1:
            bro = bro + 1
        if  bro == a:
            enemies.remove(bruh)
            display_surface.blit(nice, (358, 170))
            catches = catches + 1
            pygame.display.update()
            print(catches)
            bro = 0
            time.sleep(2)
        if len(enemies) > 1:
            display_surface.blit(fail_small, (358, 170))
            time.sleep(3)
            enemies.clear()
        for bruh in enemies:
            display_surface.blit(cool, bruh)
            
    

        pygame.display.flip()
        pygame.display.update()
        clock.tick(1000)
        

        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
            # deactivates the pygame library 
            pygame.quit() 
            # quit the program. 
            quit() 
  

