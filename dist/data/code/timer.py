import pygame


class Timer:
    # Class attributes
    miliseconds = f"000"
    seconds = f"00"
    minutes = f"00"
    hours = f"00"
    static_time = 0
    dynamic_time = 0
    is_timer_running = False

    def __init__(self):
        self.static_time = 0
        self.dynamic_time = 0
        self.is_timer_running = False

    def count(self):
        elapsed_time = pygame.time.get_ticks()
        if not self.is_timer_running:
            self.static_time = elapsed_time
            self.is_timer_running = True
        self.dynamic_time = elapsed_time - self.static_time
        return self.dynamic_time

    def reset(self):
        self.is_timer_running = False
        self.static_time = pygame.time.get_ticks()

    @classmethod
    def count_timer(cls):
        elapsed_time = pygame.time.get_ticks()

        if not cls.is_timer_running:
            cls.static_time = elapsed_time
        cls.dynamic_time = elapsed_time - cls.static_time

        miliseconds_ = cls.dynamic_time % 1000
        seconds_ = cls.dynamic_time // 1000 % 60
        minutes_ = cls.dynamic_time // 1000 // 60 % 60
        hours_ = cls.dynamic_time // 1000 // 60 // 60

        def add_0(num):
            if len(str(num)) == 1:
                return f"0{num}"
            else:
                return f"{num}"

        cls.miliseconds = add_0(miliseconds_)
        cls.seconds = add_0(seconds_)
        cls.minutes = add_0(minutes_)
        cls.hours = add_0(hours_)

    @classmethod
    def reset_timer(cls):
        cls.is_timer_running = False
        cls.static_time = pygame.time.get_ticks()

    @classmethod
    def start_timer(cls):
        cls.is_timer_running = True
