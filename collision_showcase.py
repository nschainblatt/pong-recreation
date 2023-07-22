import pygame, sys, time

pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision Detector")

score = 0
score_list = [1, 2, 3, 4, 5]
main_font = pygame.font.SysFont("comicsans", 50)

ball_x, ball_y = 100, 100
ball_speed_x, ball_speed_y = 3, 5

player_size_x = SCREEN_WIDTH
player_size_y = 15
player_starting_x = SCREEN_WIDTH / 2 - player_size_x / 2
player_starting_y = SCREEN_HEIGHT - player_size_y

player = pygame.Rect(player_starting_x, player_starting_y, player_size_x, player_size_y)
other_speed_x, other_speed_y = 2, 3

def game():
    global other_speed_x, other_speed_y, score, score_list, ball_x, ball_y, ball_speed_x, ball_speed_y

    # BACKGROUND
    SCREEN.fill((31, 36, 42))

    # TEXT
    score_text = main_font.render(f"Score: {score}", 1, (255, 255, 255))
    SCREEN.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2, 0))
    gameover_text = main_font.render("You lost!", 1, (255, 255, 255))

    # INCREASE SPEED BASED ON SCORE
    # if len(score_list) == 0:
    #     ball_speed_x *= 1.25
    #     ball_speed_y *= 1.25
    #     other_speed_x *= 1.25
    #     score_list = [1, 2, 3, 4, 5]

    # CREATE BALL
    ball = pygame.draw.circle(SCREEN, (0, 238, 255), (ball_x, ball_y), 20)

    # ENEMY COLLISION WITH SCREEN BORDERS OR LOSE IF HITS BOTTOM
    if ball.right >= SCREEN_WIDTH or ball.left <= 0:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.bottom >= SCREEN_HEIGHT:
        SCREEN.blit(gameover_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2, SCREEN_HEIGHT / 2))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    # MOVE BALL EACH FRAME
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # CHECK COLLISION WITH PLAYER AND INCREASE SCORE IF SO
    BALL_COLLISION_TOLERANCE = 10
    if ball.colliderect(player):
        if abs(player.top - ball.bottom) < BALL_COLLISION_TOLERANCE and ball_speed_y > 0:
            ball_speed_y *= -1
            score += 1
            # score_list.pop()
            # print(score_list)
        if abs(player.bottom - ball.top) < BALL_COLLISION_TOLERANCE and ball_speed_y < 0:
            ball_speed_y *= -1
        if abs(player.right - ball.left) < BALL_COLLISION_TOLERANCE and ball_speed_x < 0:
            ball_speed_x *= -1
        if abs(player.left - ball.right) < BALL_COLLISION_TOLERANCE and ball_speed_x > 0:
            ball_speed_x *= -1    

    # MOVING PLAYER
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and player.right <= SCREEN_WIDTH:
        player.x += other_speed_x
    if keys[pygame.K_LEFT] and player.left >= 0:
        player.x -= other_speed_x

    pygame.draw.rect(SCREEN, (255, 255, 255), player)


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game()
    pygame.display.update()
