from ursina import *
from assets.prefabs.controller import FirstPersonController
from assets.prefabs.weapon import Weapon


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
    g18c = Weapon(capacity=10, name='test', model='cube', color=color.black, scale_z=.5, parent=controller, delay=.2)
    g18c.position += Vec3(.2, 0, .2)

    app.run()