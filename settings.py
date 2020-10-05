class Settings():
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 3
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed_factor = 5
        self.bullet_height = 30
        self.bullet_width = 30
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 10
        # 小卢蛋设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 1
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1