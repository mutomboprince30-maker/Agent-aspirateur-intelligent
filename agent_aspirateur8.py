import pygame
import random
import math
import time

# Initialisation Pygame
pygame.init()
pygame.mixer.init()  # pour le son

WIDTH, HEIGHT = 600, 350
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agent Intelligent Aspirateur Pro")

# Couleurs
BG_COLOR = (245, 245, 245)
CHAMBER_BORDER = (80, 80, 80)
BROWN = (139, 69, 19)
GREY = (200, 200, 200)
RED = (220, 50, 50)
SHADOW = (50, 50, 50)
DUST_COLOR = (255, 215, 0)
TEXT_COLOR = (50, 50, 50)
GREEN = (50, 200, 50)
BLACK = (0, 0, 0)  # Agent

CENTER_X = 300
CENTER_Y = 125

# Son d'aspirateur
try:
    vacuum_sound = pygame.mixer.Sound("vacuum.wav")
except:
    vacuum_sound = None

# Classe chambre
class Room:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.dirty = random.choice([True, False])
        self.cleaning = False
        self.clean_progress = 0
        self.color = BROWN if self.dirty else GREY
        self.dust_particles = [(random.randint(self.x+15, self.x+235),
                                random.randint(self.y+15, self.y+235),
                                random.randint(3,6)) for _ in range(25)]
        self.show_dirty_time = pygame.time.get_ticks() if self.dirty else 0

    def draw(self):
        if self.cleaning:
            r = BROWN[0] + (GREY[0]-BROWN[0])*self.clean_progress//100
            g = BROWN[1] + (GREY[1]-BROWN[1])*self.clean_progress//100
            b = BROWN[2] + (GREY[2]-BROWN[2])*self.clean_progress//100
            self.color = (r,g,b)
        pygame.draw.rect(win, self.color, (self.x, self.y, 250, 250))
        pygame.draw.rect(win, CHAMBER_BORDER, (self.x, self.y, 250, 250), 3)

        font = pygame.font.SysFont("Arial", 38, bold=True)
        text = font.render(self.name, True, BG_COLOR)
        win.blit(text, (self.x+105, self.y+110))

        status_font = pygame.font.SysFont("Arial", 24)
        status = "Sale" if self.dirty else "Propre"
        color = RED if self.dirty else GREEN
        status_text = status_font.render(status, True, color)
        win.blit(status_text, (self.x+100, self.y+150))

        # Poussières animées
        for i, (px, py, radius) in enumerate(self.dust_particles):
            if radius > 0:
                py += math.sin(pygame.time.get_ticks()/150 + i)*0.5
                self.dust_particles[i] = (px, py, radius)
                pygame.draw.circle(win, DUST_COLOR, (int(px), int(py)), int(radius))

# Classe agent
class VacuumAgent:
    def __init__(self):
        self.x = 125
        self.y = 125
        self.target_x = self.x
        self.position = "A"
        self.cleaning_room = None
        self.cleaning_time = 0

    def move_to(self, room):
        self.target_x = 125 if room.name=="A" else 425
        self.position = room.name

    def start_cleaning(self, room):
        self.cleaning_room = room
        room.cleaning = True
        room.clean_progress = 0
        self.cleaning_time = pygame.time.get_ticks()
        if vacuum_sound:
            vacuum_sound.play(-1)

    def stop_cleaning_sound(self):
        if vacuum_sound:
            vacuum_sound.stop()

    def update_position(self):
        if self.x < self.target_x:
            self.x += 6
        elif self.x > self.target_x:
            self.x -= 6

    def update_cleaning(self):
        if self.cleaning_room:
            elapsed = pygame.time.get_ticks()-self.cleaning_time
            self.cleaning_room.clean_progress = min(elapsed*100//2000,100)
            for i, (px, py, radius) in enumerate(self.cleaning_room.dust_particles):
                if radius>0:
                    dx = self.x - px
                    dy = self.y - py
                    dist = math.hypot(dx, dy)
                    if dist!=0:
                        px += dx/15
                        py += dy/15
                        radius = max(radius - 0.15,0)
                    self.cleaning_room.dust_particles[i] = (px, py, radius)
            if self.cleaning_room.clean_progress>=100:
                self.cleaning_room.dirty=False
                self.cleaning_room.cleaning=False
                self.cleaning_room.dust_particles=[]
                self.cleaning_room=None
                self.stop_cleaning_sound()

    def draw(self):
        pygame.draw.circle(win, SHADOW, (self.x+5,self.y+5),40)
        pygame.draw.circle(win, RED, (self.x,self.y),40)
        pygame.draw.rect(win, BLACK, (self.x-30,self.y-25,60,20))

# Création chambres et agent
roomA = Room("A", 25,50)
roomB = Room("B", 325,50)
rooms = [roomA, roomB]
agent = VacuumAgent()

font = pygame.font.SysFont("Arial",28)
running = True
last_action_time = time.time()

while running:
    win.fill(BG_COLOR)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    # Barre statut
    dirty_count = sum(1 for r in rooms if r.dirty)
    status_text = f"Chambres sales : {dirty_count} / {len(rooms)}"
    bar_color = RED if dirty_count>0 else GREEN
    pygame.draw.rect(win, (200,200,200), (0,0,WIDTH,40))
    status_render = font.render(status_text, True, bar_color)
    win.blit(status_render, (10,5))

    # Dessin chambres
    for r in rooms:
        r.draw()

    # Mise à jour agent
    agent.update_position()
    agent.update_cleaning()
    agent.draw()

    # Logique agent (corrigée)
    if not agent.cleaning_room:
        dirty_rooms = [r for r in rooms if r.dirty]
        if dirty_rooms:
            target_room = dirty_rooms[0]
            agent.move_to(target_room)
            # L’agent doit être pratiquement arrivé pour commencer le nettoyage
            if abs(agent.x - agent.target_x) < 5:
                if pygame.time.get_ticks() - target_room.show_dirty_time > 1000:
                    agent.start_cleaning(target_room)
        else:
            agent.target_x=CENTER_X
            if time.time()-last_action_time>10:
                for r in rooms:
                    r.dirty=random.choice([True,False])
                    r.color=BROWN if r.dirty else GREY
                    r.dust_particles=[(random.randint(r.x+15,r.x+235),
                                        random.randint(r.y+15,r.y+235),
                                        random.randint(3,6)) for _ in range(25)]
                    if r.dirty:
                        r.show_dirty_time=pygame.time.get_ticks()
                last_action_time=time.time()

    # Texte action
    if agent.cleaning_room:
        action_text = font.render(f"Nettoyage chambre {agent.cleaning_room.name}...", True, TEXT_COLOR)
    else:
        action_text = font.render("Toutes les chambres sont propres.", True, TEXT_COLOR)
    win.blit(action_text,(120,310))

    pygame.display.update()
    pygame.time.delay(25)
