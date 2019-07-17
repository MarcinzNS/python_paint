import pygame, sys, random
import blockscreen, player

class Game(object):

    def __init__(self, x, y):
        #Inicjowanie
        pygame.init()
        self.x, self.y = x, y
        self.screen = pygame.display.set_mode((x*50, y*50)) # 17*11 = 187
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        # Konfiguracja
        self.max_tps = 60.0
        self.speed = 20
        self.fonts = pygame.font.SysFont("Ariel", 24)

        # Blocks
        self.block = blockscreen.Block(0, 0, (0,0,0), self.screen)

        self.listXY = []
        for y in range(self.y):
            for x in range(self.x):
                self.listXY.append([x, y])

        self.xos = "."*self.x
        self.listFunc=[]
        for k in range(self.y): self.listFunc.append(self.xos)

        '''self.listFunc = [".................",
                            ".................",
                            ".................",
                            ".................",
                            ".................",
                            ".................",
                            ".................",
                            ".................",
                            ".................",
                            ".................",
                            "................."]'''

        self.player = player.Player(0, 0, self.screen)
        self.player.maxX = x*50
        self.player.maxY = y*50
        self.orange = False
        self.colorlist = [[True,False],[False,False],[False,False],[False,False]] # Open, Colored
        self.charcolorlist = "%!?*"
        self.colortype = [(246,135,1),(241,70,62),(140,193,82),(94,81,198)]

        while True:
            # Sprawdzanie eventu przycisku
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit(0)
                    if event.key == pygame.K_a: self.player.left = True
                    if event.key == pygame.K_d: self.player.right = True
                    if event.key == pygame.K_w: self.player.top = True
                    if event.key == pygame.K_s: self.player.bottom = True
                    if event.key == pygame.K_q:
                        with open("save.txt","w") as f:
                            l=""
                            for i in self.listFunc: l+=i+"stop"
                            f.write(l)
                    if event.key == pygame.K_e:
                        with open("save.txt","r") as f:
                            l = f.read()
                            l = l[0:len(l)-4].split("stop")
                            self.listFunc = l
                    if event.key == pygame.K_1:
                        for i in range(4): self.colorlist[i][0] = False
                        self.colorlist[0][0] = True
                    if event.key == pygame.K_2:
                        for i in range(4): self.colorlist[i][0] = False
                        self.colorlist[1][0] = True
                    if event.key == pygame.K_3:
                        for i in range(4): self.colorlist[i][0] = False
                        self.colorlist[2][0] = True
                    if event.key == pygame.K_4:
                        for i in range(4): self.colorlist[i][0] = False
                        self.colorlist[3][0] = True
                    if event.key == pygame.K_SPACE:
                        for i in self.colorlist:
                            if i[0]: i[1] = True
                        self.playerPos = self.player.mypos()


            # Ticki na sec
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.max_tps:
                self.tick()
                self.tps_delta -= 1 / self.max_tps

            # Draw
            self.screen.fill((5, 5, 5))
            self.drow()
            pygame.display.flip()

    def drow(self):

        for i in range(len(self.listXY)): # self.listXY, self.listFunc
            self.block = blockscreen.Block(self.listXY[i][0]*50,self.listXY[i][1]*50,(255,0,0),self.screen)

            buff = self.listFunc[self.listXY[i][1]][self.listXY[i][0]]
            if buff == ".": self.block.chcolor((255,255,255))
            for i in range(4):
                if buff == self.charcolorlist[i]: self.block.chcolor(self.colortype[i])
            self.block.display()

        self.player.display()

    def tick(self):
        self.player.move()
        for n in range(4):
            if self.colorlist[n][1] and len(self.charcolorlist[n]) == 1:
                self.colorlist[n][1] = False
                x, y = self.playerPos
                x, y = int(x/50), int(y/50)

                buffe = ""
                for i in range(self.x):
                    if x == i: buffe += self.charcolorlist[n]
                    else: buffe += self.listFunc[y][i]
                self.listFunc[y] = buffe

if __name__ == "__main__":
    Game(20, 11)
