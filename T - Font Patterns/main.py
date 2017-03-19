import os
import pygame
import time
import random

count = 0
trigger = False
unistr = unichr(random.randint(0x25a0, 0x25ff))
textpos = (0,0)


def setup(screen, etc):
    pass

def draw(screen, etc):
    global count, trigger, unistr, textpos
    
    shift = int(etc.knob1*320-160)
    
    size = int(etc.knob2 * 260) + 5    
    font = pygame.font.Font(etc.mode_root + "/font.ttf", size)
    color = etc.color_picker()
    
    text = font.render(unistr, True, (color))     
    y = 0
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        unistr = get_unicode_character(int(etc.knob3 * 10)+1)
    
    for i in range(0,81) :
            
        #count += 1 % 81
        odd = i%2
        if odd == 0 :
            x = ((i % 9) * 160 + 80 + shift) - 160
            y = (int(i / 9) % 9) * 90 + 45 #+ (shift-70)
                
        if odd == 1 :
            x = ((i % 9) * 160 + 80) - 160
            y = (int(i / 9) % 9) * 90 + 45  
                
        textpos = text.get_rect(center = (x,y))
        screen.blit(text, textpos)
        
    trigger = False
            


def get_unicode_character(set) :
    
    if set == 0 :
        # all of them (or a lot of them...)
        return unichr(random.choice((0x0000, 0xFF00)) + random.randint(0, 0xff))
        
    if set == 1 :
        # ogham
        return unichr(random.randint(0x1680, 0x169C))
        
    if set == 2 :
        # arrows
        return unichr(random.randint(0x2190, 0x21FF))
        
    if set == 3 :
        # math
        return unichr(random.randint(0x2200, 0x22ff))
        
    if set == 4 :
        # geometric shapes
        return unichr(random.randint(0x25a0, 0x25ff))
        
    if set == 5 :
        # box drawing
        return unichr(random.randint(0x2500, 0x257f))
        
    if set == 6 :
        # Brail
        return unichr(random.randint(0x2800, 0x28FF))
        
    if set == 7 :
        # More math
        return unichr(random.randint(0x2A00, 0x2ADF))
        
    if set == 8 :
        # from math -- sharp symbols
        return unichr(random.randint(0x2A80, 0x2ABC))

    if set == 9 :
        # more arrows
        return unichr(random.randint(0x2900, 0x297F))
    
    if set == 10 :
        #chess
        return unichr(random.randint(0xE010, 0xE04F))
        
    if set == 11 :
        #Genji-mon Symbols
        return unichr(random.randint(0xF500, 0xF535))
        

