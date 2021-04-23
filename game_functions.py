import pygame
import sys


def check_keydown_event(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True


def check_keyup_event(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """响应按键和鼠标事件函数"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 鼠标单击退出按钮，退出游戏
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship):
    """刷新屏幕函数"""
    # 每次循环刷新屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 最近绘制的屏幕可见
    pygame.display.flip()
