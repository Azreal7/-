class Settings():

    def __init__(self):
        # 初始化游戏设置
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 0.7
        self.ship_limit = 2
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 2

        # 外星人设置
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示右移，-1 为左移
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.2

        # 外星人点数提高速度
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而改变的设置"""
        self.ship_speed_factor = 0.7
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.2

        # fleet_direction 为 1 表示向右
        self.fleet_direction = 1

        # 计分
        self.alien_points = 10

    def increase_speed(self, stats):
        """提高速度设置"""
        if stats.level <= 7:
            self.bullet_speed_factor *= self.speedup_scale
            self.alien_speed_factor *= self.speedup_scale
        else:
            self.alien_speed_factor += 0.1
        if stats.level % 5 == 0:
            self.bullet_width += 2
        self.bullets_allowed += 1
        self.alien_points = int(self.alien_points * self.score_scale)