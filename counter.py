import pygame.font

class Counter():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.text_color = (204, 24, 63)
        self.font = pygame.font.Font('fonts/kenvector_future_thin2.ttf', 26)
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        seconds = int(self.ai_settings.frame_count/60)
        miliseconds = int(self.ai_settings.frame_count%60)
        score_str = (str(seconds) + ":" + str(miliseconds))
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - self.ai_settings.screen_width/2 + 25
        self.score_rect.bottom = 40

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)