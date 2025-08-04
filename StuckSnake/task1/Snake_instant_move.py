import pygame
import sys
import random

# 初始化Pygame
pygame.init()
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Debug Task: Snake's Instant Move")
clock = pygame.time.Clock()

# 颜色和蛇的设置
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
yellow = (255, 255, 102)
snake_block = 20
snake_speed = 4
food_pos = [random.randrange(1, (screen_width // snake_block)) * snake_block,
            random.randrange(1, (screen_height // snake_block)) * snake_block]
food_spawn = True
score = 0
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# 蛇的初始状态
snake_pos = [100, 60]
snake_body = [[100, 60], [80, 60], [60, 60]]
direction = 'RIGHT'
change_to = direction

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

def game_loop():
    global direction, change_to, snake_pos, food_pos, food_spawn, score

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # 检查是否会因为急转弯而撞到自己
        new_direction = change_to
        if new_direction != direction:
            # 计算新位置
            temp_pos = list(snake_pos)
            if new_direction == 'UP':
                temp_pos[1] -= snake_block
            elif new_direction == 'DOWN':
                temp_pos[1] += snake_block
            elif new_direction == 'LEFT':
                temp_pos[0] -= snake_block
            elif new_direction == 'RIGHT':
                temp_pos[0] += snake_block

            if temp_pos in snake_body[1:]:
                # 撞到自己，游戏结束
                message("Game Over! Press Q-Quit", red)
                Your_score(score)
                pygame.display.update()
                # 等待用户选择退出
                game_over = True
                while game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game_over = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_over = False
                pygame.quit()
                sys.exit()

        direction = change_to
        # --- 更新蛇的位置和身体 ---
        if direction == 'UP':
            snake_pos[1] -= snake_block
        if direction == 'DOWN':
            snake_pos[1] += snake_block
        if direction == 'LEFT':
            snake_pos[0] -= snake_block
        if direction == 'RIGHT':
            snake_pos[0] += snake_block
        snake_body.insert(0, list(snake_pos))

        # 吃食物逻辑
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        # 生成新食物
        if not food_spawn:
            food_pos = [random.randrange(1, (screen_width // snake_block)) * snake_block,
                        random.randrange(1, (screen_height // snake_block)) * snake_block]
            food_spawn = True

        # 判断死亡（撞墙或撞到自己）
        if (snake_pos[0] < 0 or snake_pos[0] >= screen_width or 
            snake_pos[1] < 0 or snake_pos[1] >= screen_height or
            snake_pos in snake_body[1:]):
            message("Game Over! Press Q-Quit", red)
            Your_score(score)
            pygame.display.update()
            
            # 等待用户选择退出
            game_over = True
            while game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = False

            pygame.quit()
            sys.exit()

        # --- 绘制 ---
        screen.fill(black)
        for pos in snake_body:
            pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], snake_block, snake_block))

        # 绘制食物
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], snake_block, snake_block))
        
        # 显示分数
        Your_score(score)

        pygame.display.update()
        clock.tick(snake_speed)

game_loop()
