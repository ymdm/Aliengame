import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标
        gf.check_events(ship)
        ship.update()
        # 每次循环刷新屏幕,并让绘制的屏幕可见
        gf.update_screen(ai_setting, screen, ship)


run_game()