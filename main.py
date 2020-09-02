from ursina import *


def update():
    hovered = Text()
    if held_keys['a']:
        hovered.text = f'Hovered Entity : {mouse.hovered_entity}'


if __name__ == '__main__':
    app = Ursina()

    pass

    app.run()