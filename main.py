from ursina import *
from assets.prefabs.controller import FirstPersonController
from assets.prefabs.weapon import Weapon
from assets.prefabs.health_bar import HealthBar


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
                    texture='brick',
                    texture_scale=(32, 32),
                    collider='box',
                    filtering=None)
    g18c = Weapon(ammo=0,
                  mag_size=200,
                  magazine=200,
                  reload_delay=2,
                  name='test',
                  model='gun_pistol',
                  parent=controller,
                  texture='grass',
                  collider='cube',
                  shoot_delay=.001,
                  mode='auto',
                  position=Vec3(0, 0, 0))
    health_bar = HealthBar()

    app.run()