import pygame

a=4;
if a==3:
	file = 'jr.wav'
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy(): 
    			pygame.time.Clock().tick(10)

else: 
	print ("poda myre")
