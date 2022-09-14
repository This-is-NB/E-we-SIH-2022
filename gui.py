# # import playsound # allows the playing of sound files
# import time #download current time for sleep function
# import pygame #Library for running graphical interface
# import os 

# class imageHandler:
#   def __init__ ( self ):
#     self.pics = dict()

#   def loadFromFile ( self, filename, id=None ):
#     if id == None: id = filename
#     self.pics [ id ] = pygame.image.load ( filename ).convert()

#   def loadFromSurface ( self, surface, id ):
#     self.pics [ id ] = surface.convert_alpha()

#   def render ( self, surface, id, position = None, clear = False, size = None ):
#     if clear == True:
#       surface.fill ( (5,2,23) ) #

#     if position == None:
#       picX = int ( surface.get_width() / 2 - self.pics [ id ].get_width() / 2 )
#     else:
#       picX = position [0]
#       picY = position [1]

#     if size == None:
#       surface.blit ( self.pics [ id ], ( picX, picY ) ) #

#     else:
#       surface.blit ( pygame.transform.smoothscale ( self.pics [ id ], size ), ( picX, picY ) )
      
# #Initialises the display-------------------------------------------------------
# pygame.display.init() # Initiates the display pygame
# screen = pygame.display.set_mode((800,600), pygame.RESIZABLE) #uncomment this line for smaller window
# # screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #allows fullscreen #comment this line out for smaller window
# handler = imageHandler()

# def display():
#     for i,filename in enumerate(os.listdir('frames')):
#         handler.loadFromFile('frames/' + filename,str(i))
        
# display()

# def face():
#     A = 0
#     B = 0
#     x = 800
#     y = 600
    
#     while(True):
#         # pygame.display.update(30,300,800,600) 
#         # or replace with this line for easier coding 
#         for i in range(62):
#             handler.render ( screen, str(i) , ( A, B ), True, ( x, y ) )
#             pygame.display.update(A,B,x,y) 
#             time.sleep(0.05)
        

# face()

import os
import cv2
import time

frames = sorted(os.listdir('frames'),key=lambda x: int(x.split('.')[0]))

def main():
    while(True):
        for i,filename in enumerate(frames):
            print(filename)
            frame = cv2.imread('frames/' + filename)
            cv2.imshow('screen',frame)
            time.sleep(0.025)
            key = cv2.waitKey(1)
            if key == ord('q'):
                return
    
        # cv2.destroyAllWindows()
        
if __name__ == "__main__":
    main()

