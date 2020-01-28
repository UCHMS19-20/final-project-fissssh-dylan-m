# import pygame module in this program 
import pygame
import time
import random
  

pygame.mixer.pre_init(44100,16,2,4096)
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
X = 1000
Y = 670
  
# create the display surface object 
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y )) 

#time
clock = pygame.time.Clock()   

# set the pygame window name 
pygame.display.set_caption('Fishing Simulator') 
  
# setting images and sizes of those images
imag = pygame.image.load(r'src\img\Test_Opening.png') 
image2 = pygame.image.load(r'src\img\FishingMan.jpg')
fish1 = pygame.image.load(r'src\img\Fish1.png')
fish2 = pygame.image.load(r'C:\Users\McPower 2\Documents\GitHub\final-project-fissssh-dylan-m\src\img\Purple.png')
nice = pygame.image.load(r'src\img\nice-catch.jpg')
fail = pygame.image.load(r'src\img\Fail.png')
image = pygame.transform.scale(imag, (1000, 670))
fail_small = pygame.transform.scale(fail, (200, 200))
Fish1_Small = pygame.transform.scale(fish1, (150, 100))
Fish2_Small = pygame.transform.scale(fish2, (100, 100))

smallfont = pygame.font.SysFont("times new roman", 40)

pygame.mixer.music.load('src\Music.mp3')
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(-1)

done = False
intro_page = 1

#class for the different types of fish
class Fish:
    def __init__(self, time, clicks):
        self.t = time
        self.c = clicks

#types of fish and info
x = random.randint(5000,10000)
y = random.randint(10000,15000)
blue = Fish(x, 10)    
red = Fish(y, 20)    


def score(score):
    text = smallfont.render("Number of Fish Caught: "+ str(score), True, black)
    display_surface.blit(text, [0,0])



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

#just variables y'know
enemies = []
catches = 0
bro = 0
fish1_event = pygame.USEREVENT + 1
a = 1

#fish spawn timer
pygame.time.set_timer(fish1_event, blue.t)


# infinite loop 
while True : 
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method.
    display_surface = pygame.display.set_mode((1000, 670 ))
    display_surface.blit(image2, (0, 0))
    score(catches)
    for event in pygame.event.get(): 
        
        #getting keys pressed
        pressed = pygame.key.get_pressed()
        
        if event.type == fish1_event:
            #when timer hits, percent chance to get one of the types of fish
            if random.choice([0,3]) != 0:
                bruh = Fish1_Small.get_rect(topleft=(random.randrange(600), 400))
                cool = Fish1_Small
                a = 1
                # 15 for challenging
            else: 
                bruh = Fish2_Small.get_rect(topleft=(random.randrange(600), 400))
                cool = Fish2_Small
                a = 10
                #30 for challenge
            #add fish to enemies list
            enemies.append(bruh)
            # print(enemies)
        # measures amount of space key presses while fish is spawned
        if pressed[pygame.K_SPACE] and len(enemies) == 1:
            bro = bro + 1
        # once space bar pressed enough times, the fish is removed, it congragulates you, and resets it
        if  bro == a:
            enemies.remove(bruh)
            display_surface.blit(nice, (358, 170))
            catches = catches + 1
            pygame.display.update()
            print(catches)
            bro = 0
            time.sleep(1)
        #if cant catch the fish in time, shows fail screen
        if len(enemies) > 1:
            display_surface.blit(fail_small, (358, 70))
            pygame.display.update()
            time.sleep(2)
            enemies.clear()
        for bruh in enemies:
            display_surface.blit(cool, bruh)
            
    
        #just updating the visuals and time
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
  

