import pygame
import sys
import os

# Inicialitzar Pygame
pygame.init()

# Constants
AMPLE = 800
ALT = 600
FPS = 60

# Colors
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
VERMELL = (255, 0, 0)
VERD = (0, 255, 0)
BLAU = (0, 0, 255)
GROC = (255, 255, 0)

# Crear finestra
pantalla = pygame.display.set_mode((AMPLE, ALT))
pygame.display.set_caption("Arkanoid")
rellotge = pygame.time.Clock()

# Carregar imatges (canviar aquestes rutes segons les teves imatges)
try:
    img_pala = pygame.image.load("pala.png")
    img_pilota = pygame.image.load("pilota.png")
    img_totxo = pygame.image.load("totxo.png")
    
    # Redimensionar imatges si cal
    img_pala = pygame.transform.scale(img_pala, (100, 20))
    img_pilota = pygame.transform.scale(img_pilota, (15, 15))
    img_totxo = pygame.transform.scale(img_totxo, (75, 30))
except:
    # Si no es troben les imatges, utilitzarem rectangles de colors
    img_pala = None
    img_pilota = None
    img_totxo = None

# Classe Pala
class Pala:
    def __init__(self):
        self.ample = 100
        self.alt = 20
        self.x = AMPLE // 2 - self.ample // 2
        self.y = ALT - 50
        self.velocitat = 8
        self.rect = pygame.Rect(self.x, self.y, self.ample, self.alt)
        
    def moure(self, direccio):
        if direccio == "esquerra" and self.x > 0:
            self.x -= self.velocitat
        elif direccio == "dreta" and self.x < AMPLE - self.ample:
            self.x += self.velocitat
        self.rect.x = self.x
        
    def dibuixar(self):
        if img_pala:
            pantalla.blit(img_pala, (self.x, self.y))
        else:
            pygame.draw.rect(pantalla, BLAU, self.rect)

# Classe Pilota
class Pilota:
    def __init__(self):
        self.radi = 8
        self.x = AMPLE // 2
        self.y = ALT // 2
        self.vel_x = 5
        self.vel_y = -5
        self.activa = False
        self.rect = pygame.Rect(self.x - self.radi, self.y - self.radi, 
                                self.radi * 2, self.radi * 2)
        
    def moure(self):
        if self.activa:
            self.x += self.vel_x
            self.y += self.vel_y
            
            # Rebotar amb les parets
            if self.x <= self.radi or self.x >= AMPLE - self.radi:
                self.vel_x = -self.vel_x
            if self.y <= self.radi:
                self.vel_y = -self.vel_y
                
            self.rect.x = self.x - self.radi
            self.rect.y = self.y - self.radi
            
    def reiniciar(self):
        self.x = AMPLE // 2
        self.y = ALT // 2
        self.vel_x = 5
        self.vel_y = -5
        self.activa = False
        
    def dibuixar(self):
        if img_pilota:
            pantalla.blit(img_pilota, (self.x - self.radi, self.y - self.radi))
        else:
            pygame.draw.circle(pantalla, VERMELL, (int(self.x), int(self.y)), self.radi)

# Classe Totxo
class Totxo:
    def __init__(self, x, y, color):
        self.ample = 75
        self.alt = 30
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, self.ample, self.alt)
        self.destruït = False
        
    def dibuixar(self):
        if not self.destruït:
            if img_totxo:
                pantalla.blit(img_totxo, (self.x, self.y))
            else:
                pygame.draw.rect(pantalla, self.color, self.rect)
                pygame.draw.rect(pantalla, NEGRE, self.rect, 2)

# Crear totxos
def crear_totxos():
    totxos = []
    colors = [VERMELL, GROC, VERD, BLAU, VERMELL, GROC]
    
    for fila in range(6):
        for columna in range(10):
            x = columna * 80 + 5
            y = fila * 35 + 50
            totxo = Totxo(x, y, colors[fila])
            totxos.append(totxo)
    
    return totxos

# Funció principal del joc
def main():
    # Crear objectes
    pala = Pala()
    pilota = Pilota()
    totxos = crear_totxos()
    
    # Variables del joc
    puntuacio = 0
    vides = 3
    font = pygame.font.Font(None, 36)
    joc_iniciat = False
    
    # Bucle principal
    jugant = True
    while jugant:
        rellotge.tick(FPS)
        
        # Gestionar esdeveniments
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugant = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not pilota.activa:
                    pilota.activa = True
                    joc_iniciat = True
        
        # Obtenir tecles premudes
        tecles = pygame.key.get_pressed()
        if tecles[pygame.K_LEFT]:
            pala.moure("esquerra")
        if tecles[pygame.K_RIGHT]:
            pala.moure("dreta")
        
        # Moure pilota
        pilota.moure()
        
        # Col·lisió pilota-pala
        if pilota.rect.colliderect(pala.rect) and pilota.vel_y > 0:
            pilota.vel_y = -pilota.vel_y
            # Afegir efecte segons on toca la pala
            diferencia = pilota.x - (pala.x + pala.ample // 2)
            pilota.vel_x = diferencia // 5
        
        # Col·lisió pilota-totxos
        for totxo in totxos:
            if not totxo.destruït and pilota.rect.colliderect(totxo.rect):
                totxo.destruït = True
                pilota.vel_y = -pilota.vel_y
                puntuacio += 10
                break
        
        # Comprovar si la pilota cau
        if pilota.y > ALT:
            vides -= 1
            if vides > 0:
                pilota.reiniciar()
            else:
                # Game Over
                joc_iniciat = False
                totxos = crear_totxos()
                vides = 3
                puntuacio = 0
                pilota.reiniciar()
        
        # Comprovar victòria
        totxos_restants = sum(1 for t in totxos if not t.destruït)
        if totxos_restants == 0:
            totxos = crear_totxos()
            pilota.reiniciar()
        
        # Dibuixar tot
        pantalla.fill(NEGRE)
        
        # Dibuixar totxos
        for totxo in totxos:
            totxo.dibuixar()
        
        # Dibuixar pala i pilota
        pala.dibuixar()
        pilota.dibuixar()
        
        # Dibuixar informació
        text_puntuacio = font.render(f"Punts: {puntuacio}", True, BLANC)
        text_vides = font.render(f"Vides: {vides}", True, BLANC)
        pantalla.blit(text_puntuacio, (10, 10))
        pantalla.blit(text_vides, (AMPLE - 150, 10))
        
        # Missatge inicial
        if not joc_iniciat:
            font_gran = pygame.font.Font(None, 48)
            text_inici = font_gran.render("Prem ESPAI per començar", True, BLANC)
            rect_text = text_inici.get_rect(center=(AMPLE // 2, ALT // 2))
            pantalla.blit(text_inici, rect_text)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()