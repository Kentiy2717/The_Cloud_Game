from random import choice, randint
import sys

import pygame as pg

from constants import (
    BOARD_BACKGROUND_COLOR,
    DOWN, LEFT, RIGHT, UP,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SPEED,
    GRID_SIZE,
    GRID_WIDTH,
    GRID_HEIGHT,
    RED, GREEN, BLUE,
    SCREEN_CENTER
)

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Центр игрового поля
SCREEN_CENTER = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]

# Заголовок окна игрового поля:
pg.display.set_caption('The Game')

# Настройка времени:
clock = pg.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """Базовый класс для наследования"""

    def __init__(self,
                 body_color_value=None,
                 position_value=SCREEN_CENTER,
                 foreground_color=BOARD_BACKGROUND_COLOR
                 ) -> None:
        # Цвет объекта, поумолчанию не определён.
        self.body_color = body_color_value
        # Цвет бордера, поумолчанию FOREGOUND_COLOR.
        self.foreground_color = foreground_color
        # Позиция объекта, поумолчанию центральная точка экрана.
        self.position = position_value

    def draw(
            self,
            surface,
            position_value,
            body_color_value,
            foreground_color_value):
        """Заготовка метода отрисовки объекта на игровом поле"""
        rect = pg.Rect(
            (position_value[0], position_value[1]),
            (GRID_SIZE, GRID_SIZE)
        )
        pg.draw.rect(surface, body_color_value, rect)
        pg.draw.rect(surface, foreground_color_value, rect, 1)


def handle_keys(game_object):
    """Функция обработки нажатия клавиш"""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pg.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pg.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pg.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT
            elif event.key == pg.K_ESCAPE:
                sys.exit()


def main():
    """Функция основного цикла игры"""
    # Инициализация pg:
    pg.init()
    game_object = GameObject()

    while True:
        global SPEED
        clock.tick(SPEED)

        # Тут опишите основную логику игры.
        handle_keys(game_object)
        pg.display.update()


if __name__ == "__main__":
    main()
