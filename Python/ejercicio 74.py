import pygame
import sys
import random

# Inicialitzar pygame
pygame.init()

# Constants
AMPLADA = 800
ALÇADA = 600
FPS = 60

# Colors
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
VERMELL = (255, 0, 0)
BLAU = (0, 0, 255)
VERD = (0, 255, 0)
GROC = (255, 255, 0)

# Crear finestra
pantalla = pygame.display.set_mode((AMPLADA, ALÇADA))
pygame.display.set_caption("Arkanoid")
rellotge = pygame.time.Clock()

# Carregar imatges (canvia la ruta segons les teves imatges)
try:
    imatge_pala = pygame.image.load("/home/cicles/AO/Tasca11/pala.png")
    imatge_pilota = pygame.image.load("/home/cicles/AO/Tasca11/pilota.png")
    imatge_totxo = pygame.image.load("/home/cicles/AO/Tasca11/totxo.png")
except:
    # Si no es troben les imatges, crear superfícies de colors
    imatge_pala = pygame.Surface((100, 20))
    imatge_pala.fill(BLAU)
    
    imatge_pilota = pygame.Surface((15, 15))
    imatge_pilota.fill(VERMELL)
    
    imatge_totxo = pygame.Surface((75, 30))
    imatge_totxo.fill(VERD)

# Classe Pala
class Pala:
    def __init__(self):
        self.imatge = pygame.transform.scale(imatge_pala, (100, 20))
        self.rect = self.imatge.get_rect()
        self.rect.centerx = AMPLADA // 2
        self.rect.bottom = ALÇADA - 30
        self.velocitat = 8
    
    def moure(self, direccio):
        if direccio == "esquerra" and self.rect.left > 0:
            self.rect.x -= self.velocitat
        elif direccio == "dreta" and self.rect.right < AMPLADA:
            self.rect.x += self.velocitat
    
    def dibuixar(self, pantalla):
        pantalla.blit(self.imatge, self.rect)

# Classe Pilota
class Pilota:
    def __init__(self, pala_rect):
        self.imatge = pygame.transform.scale(imatge_pilota, (15, 15))
        self.rect = self.imatge.get_rect()
        self.rect.centerx = pala_rect.centerx
        self.rect.bottom = pala_rect.top
        self.velocitat_x = 0
        self.velocitat_y = 0
        self.activa = False
    
    def iniciar(self, pala_rect):
        self.velocitat_x = random.choice([-4, -3, 3, 4])
        self.velocitat_y = -5
        self.activa = True
    
    def moure(self, pala_rect):
        if not self.activa:
            # La pilota segueix la pala abans de començar
            self.rect.centerx = pala_rect.centerx
            self.rect.bottom = pala_rect.top
        else:
            self.rect.x += self.velocitat_x
            self.rect.y += self.velocitat_y
            
            # Rebots amb les parets
            if self.rect.left <= 0 or self.rect.right >= AMPLADA:
                self.velocitat_x = -self.velocitat_x
            
            if self.rect.top <= 0:
                self.velocitat_y = -self.velocitat_y
    
    def dibuixar(self, pantalla):
        pantalla.blit(self.imatge, self.rect)
    
    def reset(self, pala_rect):
        self.rect.centerx = pala_rect.centerx
        self.rect.bottom = pala_rect.top
        self.velocitat_x = 0
        self.velocitat_y = 0
        self.activa = False

# Classe Totxo
class Totxo:
    def __init__(self, x, y, color):
        self.imatge = pygame.transform.scale(imatge_totxo, (75, 30))
        # Aplicar un tint de color
        self.imatge.fill(color, special_flags=pygame.BLEND_MULT)
        self.rect = self.imatge.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.viu = True
    
    def dibuixar(self, pantalla):
        if self.viu:
            pantalla.blit(self.imatge, self.rect)

# Crear nivell de totxos
def crear_totxos():
    totxos = []
    colors = [VERMELL, GROC, VERD, BLAU, (255, 165, 0), (128, 0, 128)]
    
    for fila in range(6):
        for columna in range(10):
            x = columna * 80 + 5
            y = fila * 35 + 50
            color = colors[fila % len(colors)]
            totxo = Totxo(x, y, color)
            totxos.append(totxo)
    
    return totxos

# Funció principal del joc
def main():
    # Crear objectes
    pala = Pala()
    pilota = Pilota(pala.rect)
    totxos = crear_totxos()
    
    # Variables del joc
    puntuacio = 0
    vides = 3
    joc_iniciat = False
    font = pygame.font.Font(None, 36)
    font_gran = pygame.font.Font(None, 72)
    
    executant = True
    
    while executant:
        # Gestionar events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executant = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not pilota.activa:
                    pilota.iniciar(pala.rect)
                    joc_iniciat = True
        
        # Obtenir tecles pressionades
        tecles = pygame.key.get_pressed()
        if tecles[pygame.K_LEFT]:
            pala.moure("esquerra")
        if tecles[pygame.K_RIGHT]:
            pala.moure("dreta")
        
        # Moure pilota
        pilota.moure(pala.rect)
        
        # Comprovar col·lisió amb la pala
        if pilota.activa and pilota.rect.colliderect(pala.rect):
            pilota.velocitat_y = -abs(pilota.velocitat_y)
            # Ajustar angle segons on impacta
            diferencia = pilota.rect.centerx - pala.rect.centerx
            pilota.velocitat_x += diferencia // 10
            # Limitar velocitat
            pilota.velocitat_x = max(-7, min(7, pilota.velocitat_x))
        
        # Comprovar col·lisió amb totxos
        for totxo in totxos:
            if totxo.viu and pilota.activa and pilota.rect.colliderect(totxo.rect):
                totxo.viu = False
                pilota.velocitat_y = -pilota.velocitat_y
                puntuacio += 10
        
        # Comprovar si la pilota cau
        if pilota.rect.top > ALÇADA:
            vides -= 1
            if vides > 0:
                pilota.reset(pala.rect)
            else:
                # Game Over
                joc_iniciat = False
        
        # Comprovar victòria
        totxos_vius = sum(1 for totxo in totxos if totxo.viu)
        if totxos_vius == 0:
            totxos = crear_totxos()
            pilota.reset(pala.rect)
        
        # Dibuixar
        pantalla.fill(NEGRE)
        
        # Dibuixar tots els elements
        pala.dibuixar(pantalla)
        pilota.dibuixar(pantalla)
        
        for totxo in totxos:
            totxo.dibuixar(pantalla)
        
        # Dibuixar interfície
        text_puntuacio = font.render(f"Puntuació: {puntuacio}", True, BLANC)
        text_vides = font.render(f"Vides: {vides}", True, BLANC)
        pantalla.blit(text_puntuacio, (10, ALÇADA - 40))
        pantalla.blit(text_vides, (AMPLADA - 150, ALÇADA - 40))
        
        # Missatge inicial
        if not joc_iniciat:
            if vides > 0:
                text_inici = font.render("Prem ESPAI per començar", True, BLANC)
                pantalla.blit(text_inici, (AMPLADA//2 - 200, ALÇADA//2))
            else:
                text_game_over = font_gran.render("GAME OVER", True, VERMELL)
                pantalla.blit(text_game_over, (AMPLADA//2 - 200, ALÇADA//2 - 50))
                text_reiniciar = font.render("Tanca per sortir", True, BLANC)
                pantalla.blit(text_reiniciar, (AMPLADA//2 - 150, ALÇADA//2 + 50))
        
        # Actualitzar pantalla
        pygame.display.flip()
        rellotge.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()