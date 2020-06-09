# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)

# Set the height and width of the screen
size  = [400,300]
screen= pygame.display.set_mode(size)
font= pygame.font.SysFont("consolas",20)

pygame.display.set_caption("Game Title")

#Loop until the user clicks the close button.
done = False
flag = None
clock= pygame.time.Clock()

# print text function
def printText(msg, color='BLACK', pos=(50,50)):
    textSurface     = font.render(msg,True, pygame.Color(color),None)
    textRect        = textSurface.get_rect()
    textRect.topleft= pos

    screen.blit(textSurface, textRect)

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    # Main Event Loop
    for event in pygame.event.get():# User did something
        if event.type == pygame.KEYDOWN:# If user release what he pressed.
            pressed= pygame.key.get_pressed()
            buttons= [pygame.key.name(k) for k,v in enumerate(pressed) if v]
            flag = True
        elif event.type == pygame.KEYUP:# If user press any key.
            flag= False
        elif event.type == pygame.QUIT: # If user clicked close.
            done= True                 
 
     
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
      
    # Clear the screen and set the screen background
    screen.fill(WHITE)
 
    # Print red text if user pressed any key.
    if flag== True:
        printText('you just key down!!','RED')
        printText('--> you pressed any key.','RED', (50,70))
        printText('Pressed Key : ' + buttons[0],'RED', (50,90))
 
    # Print blue text if user released any key.
    elif flag== False:
        printText('you just key up!!','BLUE')
        printText('--> released what you pressed.','BLUE', (50,70))
 
    # Print default text if user do nothing.
    else:
        printText('Please press any key.')
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()