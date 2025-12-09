import pygame
import random
import sys

# Inicialización de pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")

# Colores
WHITE = (255, 255, 255)

# Cargar imágenes
try:
    paddle = pygame.image.load("paleta.png")  # Paleta (bat)
    ball = pygame.image.load("pelota.png")    # Pelota
    brick = pygame.image.load("ladrillos.png") # Ladrillos
    print("Imágenes cargadas correctamente.")
except pygame.error as e:
    print("Error al cargar las imágenes:", e)
    sys.exit()

# Redimensionar las imágenes
paddle = pygame.transform.scale(paddle, (100, 20))  # Ajustar el tamaño de la paleta
ball = pygame.transform.scale(ball, (20, 20))      # Ajustar el tamaño de la pelota
brick = pygame.transform.scale(brick, (60, 20))    # Ajustar el tamaño de los ladrillos

# Dimensiones de las imágenes
paddle_width, paddle_height = paddle.get_width(), paddle.get_height()
ball_radius = ball.get_width() // 2
brick_width, brick_height = brick.get_width(), brick.get_height()

# Posiciones iniciales
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 40
ball_x = WIDTH // 2
ball_y = HEIGHT - 50  # Asegúrate de que la pelota no esté en el borde inferior
ball_dx = 3 * random.choice((1, -1))  # Reducir la velocidad de la pelota
ball_dy = -3  # Reducir la velocidad de la pelota

# Ladrillos
bricks = []
for row in range(5):
    for col in range(10):
        brick_rect = pygame.Rect(col * (brick_width + 5) + 50, row * (brick_height + 5) + 50, brick_width, brick_height)
        bricks.append(brick_rect)

# Función para dibujar la paleta, la pelota y los ladrillos
def draw_window():
    WIN.fill(WHITE)  # Limpiar la pantalla
    WIN.blit(paddle, (paddle_x, paddle_y))  # Dibujar la paleta
    WIN.blit(ball, (ball_x - ball_radius, ball_y - ball_radius))  # Dibujar la pelota
    
    for brick_rect in bricks:
        WIN.blit(brick, brick_rect)  # Dibujar cada ladrillo en su posición

    pygame.display.update()  # Actualizar la pantalla

# Función principal del juego
def main():
    global paddle_x, ball_x, ball_y, ball_dx, ball_dy, bricks
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)  # FPS (cuadros por segundo)

        # Comprobar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Mover la paleta con las flechas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= 5
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
            paddle_x += 5

        # Mover la pelota
        ball_x += ball_dx
        ball_y += ball_dy

        # Rebote de la pelota con las paredes
        if ball_x <= 0 or ball_x >= WIDTH:
            ball_dx = -ball_dx
        if ball_y <= 0:
            ball_dy = -ball_dy
        if ball_y >= HEIGHT:
            print("La pelota tocó el fondo. Fin del juego.")
            run = False  # El juego termina si la pelota toca el fondo

        # Rebote de la pelota con la paleta
        if paddle_y < ball_y + ball_radius < paddle_y + paddle_height and paddle_x < ball_x < paddle_x + paddle_width:
            ball_dy = -ball_dy

        # Colisión con los ladrillos
        for brick_rect in bricks[:]:
            if brick_rect.collidepoint(ball_x, ball_y):
                ball_dy = -ball_dy
                bricks.remove(brick_rect)

        # Redibujar la ventana
        draw_window()

    pygame.quit()
    sys.exit()  # Esto asegura que el programa se cierre correctamente

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
        pygame.quit()
        sys.exit()