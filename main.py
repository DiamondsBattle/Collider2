from ursina import *
from assets.prefabs.controller import FirstPersonController


def update():
    global hovered, position
    if held_keys['a']:
        hovered.text = f'Hovered Entity : {mouse.hovered_entity}'
    else:
        hovered.text = ''
    if held_keys['e']:
        position.text = f'X : {controller.position[0]} Y : {controller.position[1]} Z : {controller.position[2]}'
    else:
        position.text = ''


if __name__ == '__main__':
    app = Ursina()

    hovered = Text()
    position = Text(position=window.top)

    sky = Sky()
    controller = FirstPersonController()
    ground = Entity(model='plane',
                    scale=32,
                    texture='grass',
                    texture_scale=(32, 32),
                    collider='box',
                    filtering=None)

    app.run()