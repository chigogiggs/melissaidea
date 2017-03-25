import pygame
import sys, random,time
from pygame.locals import *

randomnumbers = [random.randrange(1, 100, 1) for _ in range(int(42 / 2))]
randomnumbers2 = randomnumbers.copy()
random.shuffle(randomnumbers)
totnum = randomnumbers2+randomnumbers
identitylist = [random.randrange(101, 200, 1) for ___ in range(int(42))]
tilelist =  []
width, height = 800, 700
size = (width, height)
# init your pygame
pygame.init()
screen = pygame.display.set_mode(size, DOUBLEBUF)
flags = screen.get_flags()
clock = pygame.time.Clock()

clickcheck =0
class Tiles():
    def __init__(self, number,switch,show,colo = 'red'):
        self.id = number
        self.switch = switch
        self.show = show
        self.color = colo
        self.identity = random.choice(identitylist)
        identitylist.remove(self.identity)
        self.life = 'alive'
        self.blue = 0

    def getIdentity(self):
        return  self.identity
    def killl(self):
        self.life = 'dead'

    def unsetBlue(self):
        if self.blue == 1:
            self.blue = 0

            print('blue off')

    def getlife(self):
        return self.life

    def getID(self):
        return self.id

    def setcol(self,col):
        self.color = col

    def setBlue(self):
        self.blue = 1
        print('blue on')

    def shownumber(self):
        if self.show == 0:
            self.show = 1
            print('on')
    def dontshownumber(self):
        if self.show == 1:
            self.show= 0
            print('off')

    def switchstatusoff(self):
        if self.switch == 0:
            self.switch = 1

    def writee(self,text,pos):
        text =  str(text)
        font = pygame.font.SysFont('Lucida Grande', 36)
        text = font.render(text, 1, (255, 255, 255))
        screen.blit(text, pos)
    def drawTile(self,x, y ):
        self.x = x
        # self.switch = switch
        color = self.color
        self.y = y
        if color == 'red':
            loadtile = pygame.image.load('redtile.png')
            if self.switch == 1:
                loadtile = loadtile.convert()
                loadtile.set_alpha(0)

            loadtile = pygame.transform.scale(loadtile, (100, 100))
            screen.blit(loadtile, (self.x, self.y))
        if color == 'green':
            loadtile = pygame.image.load('greentile.png')
            if self.switch == 1:
                loadtile = loadtile.convert()
                loadtile.set_alpha(0)


            loadtile = pygame.transform.scale(loadtile, (100, 100))
            screen.blit(loadtile, (self.x, self.y))

        #
        # if color == 'blue':
        #     loadtile = pygame.image.load('blue.png')
        #     if self.switch == 1:
        #         loadtile = loadtile.convert()
        #         loadtile.set_alpha(0)
        #
        #     loadtile = pygame.transform.scale(loadtile, (100, 100))
        #     screen.blit(loadtile, (self.x, self.y))
        if self.blue == 1:
            loadtile = pygame.image.load('blue.png')

            if self.switch == 1:
                loadtile = loadtile.convert()
                loadtile.set_alpha(0)

            loadtile = pygame.transform.scale(loadtile, (100, 100))
            screen.blit(loadtile, (self.x, self.y))


        if color == 'white':
            loadtile = pygame.image.load('whitetile.png')
            if self.switch == 1:
                loadtile = loadtile.convert()
                loadtile.set_alpha(0)

            loadtile = pygame.transform.scale(loadtile, (100, 100))
            screen.blit(loadtile, (self.x, self.y))

        if self.show == 1:
            self.writee(self.id,(self.x+25,self.y+25))


        return self.x,self.y


for i in totnum:
    tilelist.append(Tiles(i,0,0))

bg = pygame.image.load('bg.jpg')
bg =  pygame.transform.scale(bg, (700, 600))

matchinglist = []


def set_init_fullScreen():
    global flags
    if flags & FULLSCREEN == False:
        flags |= FULLSCREEN
        pygame.display.set_mode(size, flags)
samecheck = []
samecheck2 = []
exilee = []
tobered = []
def mainLoop():
    timer = 0
    global flags,timer
    while True:
        timer += 1
        # print(timer)
        if timer >= 50:

            timer=0
            try:
                if len(tobered) %2 == 0:
                    print('TIMER!!')
                    tobered[0].unsetBlue()
                    tobered[1].unsetBlue()
                    tobered[0].dontshownumber()
                    tobered[1].dontshownumber()
                    tobered.pop(0)
                    tobered.pop(0)
            except Exception as e:
                print(e)

        global clickcheck
        tilex, tiley  = 50,50
        global tiley,tilex
        clock.tick(60)
        screen.fill((255, 255, 80))
        screen.blit(bg, (50, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    flags ^= FULLSCREEN
                    pygame.display.set_mode(size, flags)
                elif event.key ==K_f:
                    if flags&FULLSCREEN==False:
                        flags|=FULLSCREEN
                        pygame.display.set_mode(size, flags)
                    else:
                        flags^=FULLSCREEN
                        pygame.display.set_mode(size, flags)
        mouse = pygame.mouse.get_pos()
        mousepressed = pygame.mouse.get_pressed()
        # print(mousepressed)

        for tile in tilelist:
            tileindex = tilelist.index(tile)
            oldtile = tilelist[tileindex-1]
            oldtile2 = tilelist[tileindex-2]




            if mouse[0] in range(tilex, tilex + 100) and mouse[1] in range(tiley, tiley + 100):

                tile.setcol( 'green')

                if mousepressed[0] == 1:
                    # try:

                    print('--------------------------------')
                    identity = tile.getIdentity()
                    idd = tile.getID()
                    life = tile.getlife()
                    tile.shownumber()
                    if life == 'alive':
                        samecheck.append(identity)
                        samecheck2.append(identity)
                        matchinglist.append(idd)
                        exilee.append(tile)
                        print('identity',idd,'=', identity)
                        print('matchlist ',matchinglist)

                        tile.setcol('white')
                        tile.setBlue()
                        print('samecheck ',samecheck)

                        try:
                            if len(samecheck) > 1:
                                if samecheck[-1] == samecheck[-2]:
                                    print('poping ', matchinglist[-1])
                                    samecheck.pop(-1)
                                    matchinglist.pop(-1)
                                    exilee.pop(-1)
                                    print('new matchinglist ', matchinglist)

                        except IndexError:
                            pass

                        if len(matchinglist) == 2:
                            if matchinglist[0] == matchinglist[1]:
                                print('exile ', len(exilee))
                                exilee[1].shownumber()
                                exilee[0].shownumber()
                                time.sleep(0.3)
                                exilee[1].switchstatusoff()
                                exilee[0].switchstatusoff()
                                exilee[1].killl()
                                exilee[0].killl()
                                exilee[:] = []
                                samecheck[:] = []
                                samecheck2[:] = []
                                try:
                                    tobered[0].unsetBlue()
                                    tobered[1].unsetBlue()
                                except:pass
                            else:
                                print('sent to tobered')
                                tobered.append(exilee[0])
                                tobered.append(exilee[1])
                                print(len(tobered))


                    if len(matchinglist) == 2:
                        matchinglist[:] = []
                    if len(samecheck) ==2:
                        samecheck[:] = []

            else:
                tile.setcol('red')
            tile.drawTile(tilex, tiley )
            tilex += 100


            if (tilex-50)%700 ==0:
                tiley += 100
                tilex = 50
        if len(exilee) == 2:
            exilee[:] = []

        pygame.display.update()

# tile('red')
# set_init_fullScreen()
mainLoop()