import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats
from pygame.sprite import Group
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 创建一个游戏窗口并显示大小
    pygame.display.set_caption("阻止小卢蛋入侵")

    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_activate:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()  # 使绘制的屏幕可见


run_game()
