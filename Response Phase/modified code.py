# -*- coding: utf-8 -*-
import pygame

name = raw_input("enter text")
a="കമ്പ്യൂട്ടർ സയൻസ് ഡിപ്പാർട്ട്മെന്റിലേക്കുള്ള വഴി എങ്ങനെയാണ്";
b="സിവിൽ ഡിപ്പാർട്ട്മെന്റിലേക്കുള്ള വഴി എങ്ങനെയാണ് ";
c="ഇലക്ട്രോണിക്സ് ഡിപ്പാർട്ട്മെന്റിലേക്കുള്ള വഴി എങ്ങനെയാണ് ";
d="ആർക്കിടെക്ചർ ഡിപ്പാർട്ട്മെന്റിലേക്കുള്ള വഴി എങ്ങനെയാണ്";
e="മെക്കാനിക്കൽ ഡിപ്പാർട്ട്മെന്റിലേക്കുള്ള വഴി എങ്ങനെയാണ്";
if name == a:
	file = 'jr1.wav'
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy(): 
    			pygame.time.Clock().tick(10)

elif name == b: 
	file = 'jr2.wav'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
                        pygame.time.Clock().tick(10)
elif name == c:
	file = 'jr3.wav'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
                        pygame.time.Clock().tick(10)
elif name == d:
	file = 'jr4.wav'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
                        pygame.time.Clock().tick(10)
elif name == e:
	file = 'jr5.wav'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
                        pygame.time.Clock().tick(10)
 
else :
 	print("Invalid")
