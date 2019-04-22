#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import environ, path
from pocketsphinx import *
from sphinxbase import *

MODELDIR = "/home/gokul/Desktop/project/sofie/model"
DATADIR = "/home/gokul/Desktop/project/sofie/data"

config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, '.'))
config.set_string('-lm', path.join(MODELDIR, 'ml.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'ml.dic'))
config.set_string('-logfn', '/dev/null')
decoder = Decoder(config)

listing = ["കമ്പ്യൂട്ടർ സയൻസ് ഡിപ്പാർട്ട്മെന്റിലേക്കുള്ള വഴി എങ്ങനെയാണ്", 
"സിവിൽ ഡിപ്പാർട്ട്മെന്റിലേക്കുള്ള വഴി എങ്ങനെയാണ്", 
"ഇലക്ട്രോണിക്സ് ഡിപ്പാർട്ട്മെന്റിലേക്കുള്ള വഴി എങ്ങനെയാണ്", 
"ആർക്കിടെക്ചർ ഡിപ്പാർട്ട്മെന്റിലേക്കുള്ള വഴി എങ്ങനെയാണ്", 
"മെക്കാനിക്കൽ ഡിപ്പാർട്ട്മെന്റിലേക്കുള്ള വഴി എങ്ങനെയാണ്", 
"ഇലക്ട്രിക്കൽ ഡിപ്പാർട്ട്മെന്റിലേക്കുള്ള വഴി എങ്ങനെയാണ്", 
"ഈ കോളേജിൽ എത്ര ഡിപ്പാർട്ട്മെന്റുകൾ ഉണ്ട്", 
"കമ്പ്യൂട്ടർ സയൻസ് ഡിപ്പാർട്ട്മെന്റിലെ എച്ച്ഓഡി ആരാണ്", 
"ഇലക്ട്രിക്കൽ ഡിപ്പാർട്ട്മെന്റിലെ എച്ച്ഓഡി ആരാണ്", 
"ഇലക്ട്രോണിക്സ് ഡിപ്പാർട്ട്മെന്റിലെ എച്ച്ഓഡി ആരാണ്", 
"ആർക്കിടെക്ചർ ഡിപ്പാർട്ട്മെന്റിലെ എച്ച്ഓഡി ആരാണ്", 
"മെക്കാനിക്കൽ ഡിപ്പാർട്ട്മെന്റിലെ എച്ച്ഓഡി ആരാണ്", 
"സിവിൽ ഡിപ്പാർട്ട്മെന്റിലെ എച്ച്ഓഡി ആരാണ്", 
"കോളേജ് സ്ഥാപിച്ച വർഷം ഏതാണ്", 
"കോളേജിലെ ടെക്നിക്കൽ ഫെസ്റ്റ്ന്റെ പേരെന്താണ്", 
"പ്രിന്സിപ്പാളിന്റെ പേരെന്താണ്", 
"കോളേജ് ഓഫീസ് എവിടെയാണ്", 
"കോളേജിലെ ഡിപ്പാർട്ട്മെന്റ് ഏതൊക്കെ", 
"കോളേജ് നിലവിൽ വന്ന വർഷം ഏത്", 
"കോളേജ് സ്ഥാപിതമായ വർഷം ഏത്", 
"ഇവിടെ പാർട്ടൈം ബീട്ടെക്ക് കോഴ്സുകൾ ഉണ്ടോ", 
"ഇവിടെ ഹോസ്റ്റൽ സൗകര്യം ലഭ്യമാണോ", 
"കോളേജ് ഏത് സർവകലാശാലയ്ക്ക് കീഴിലാണ് പ്രവർത്തിക്കുന്നത്", 
"കോളേജിന്റെ ആദർശസുക്തം എന്താണ്", 
"ഇവിടെ ആകെ എത്ര വിദ്യാർഥികൾ ഉണ്ട്", 
"ഇവിടെ ആകെ എത്ര അധ്യാപകർ ഉണ്ട്", 
"കോളേജിലെ വെബ്സൈറ്റ് ഏതാണ്"]

import pygame
def response_output(indexof):
    file = str(indexof)+'.wav'
    print "outputing file :", file
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
                pygame.time.Clock().tick(1)

def result_valid_check(text):
    if text in listing:
        #print 'Result: ',listing.index(text)
        response_output(listing.index(text))
    else:
        print "not found"

import pyaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()
in_speech_bf = False
decoder.start_utt()
while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()
                print 'Result:', decoder.hyp().hypstr
                result_valid_check(decoder.hyp().hypstr)
                decoder.start_utt()
    else:
        break
decoder.end_utt()
