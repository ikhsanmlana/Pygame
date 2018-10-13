class Settings():
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 750
        self.bg_color = (255, 255, 255)

        self.ship_speed_factor = 3.0
        self.ship_limit = 3

        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,0,255)
        self.bullets_allowed = 3

        self.alien_speed_factor = 2
        self.fleet_drop_speed = 6
        self.fleet_direction =  1

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 3.0
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 2

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)