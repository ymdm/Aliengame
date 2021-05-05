import pygame
import sys
from bullet import Bullet


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        # 按Q建退出游戏
        sys.exit()


def check_keyup_event(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件函数"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 鼠标单击退出按钮，退出游戏
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship, bullets,alien):
    """刷新屏幕函数"""
    # 每次循环刷新屏幕，显示子弹与飞船位置
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
    # 最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    # 删除消失的子弹,并更新子弹坐标
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹，并将其加入到编组bullets中,创建前先检测子弹是否超过数量限制
    if len(bullets) < ai_settings.bullet_allows:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
