# Write your code here :-)
import pgzrun
import pygame
from random import randint
import math

WIDTH = 1200 # Width of window
HEIGHT = 800 # Height of window
SPEED = 4

new_width = 80
new_height = 80

letter = Actor("letter")
letter._surf = pygame.transform.scale(letter._surf, (new_width, new_height))
letter._update_pos()

def draw():
    screen.clear()
    letter.draw()

    # screen.blit('background', (0, 0))
    #player.image = player.images[math.floor(player.status/6)]
    #player.draw()
    #drawLasers()
    #drawLetters()
    drawBases()
    #screen.draw.text(str(score) , topright=(780, 10), owidth=0.5, ocolor=(255,255,255), color=(0,64,255) , fontsize=60)
    #if player.status >= 30:
    #    screen.draw.text("GAME OVER\nPress Enter to play again" , center=(400, 300), owidth=0.5, ocolor=(255,255,255), color=(255,64,0) , fontsize=60)
    #if len(aliens) == 0 :
    #    screen.draw.text("YOU WON!\nPress Enter to play again" , center=(400, 300), owidth=0.5, ocolor=(255,255,255), color=(255,64,0) , fontsize=60)


def update():
    letter.y += SPEED
    #letter.width = 25
    #letter.height = 25

def drawLetters():
    for l in range(len(letters)): letters[l].draw()

def drawBases():
    for b in range(len(bases)): bases[b].drawClipped()

def drawLasers():
    for l in range(len(lasers)): lasers[l].draw()

def fire_letter():
    letter.pos = randint(0, WIDTH), 0
    print(letter.pos)


def init():
    global lasers, score, player, moveSequence, moveCounter, moveDelay
    initLetters()
    initBases()
    #moveCounter = moveSequence = player.status = score = player.laserCountdown = 0
    #lasers = []
    #moveDelay = 30
    #player.images = ["player","explosion1","explosion2","explosion3","explosion4","explosion5"]
    #player.laserActive = 1

def initLetters():
    global letters
    letters = []
    for l in range(26):
        letters.append(Actor("letter", (randint(0, WIDTH), 0)))
        letters[l].status = 0
        letters[l].width = 25
        letters[l].height = 25
        print(letters[l].x, letters[l].y, letters[l].width, letters[l].height)

def drawClipped(self):
    screen.surface.blit(self._surf, (self.x-32, self.y-self.height+30),(0,0,64,self.height))

def collideLaser(self, other):
    return (
        self.x-20 < other.x+5 and
        self.y-self.height+30 < other.y and
        self.x+32 > other.x+5 and
        self.y-self.height+30 + self.height > other.y
    )

def initBases():
    global bases
    bases = []
    bc = 0
    for b in range(3):
        for p in range(3):
            bases.append(Actor("base1", midbottom=(150+(b*400)+(p*40), 800)))

            bases[bc].drawClipped = drawClipped.__get__(bases[bc])
            bases[bc].collideLaser = collideLaser.__get__(bases[bc])
            bases[bc].height = 60
            bc +=1

init()
clock.schedule_interval(fire_letter, 4.0)
pgzrun.go()
