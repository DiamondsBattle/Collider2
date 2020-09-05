from ursina import *
from assets.prefabs.controller import FirstPersonController
from assets.prefabs.weapon import Weapon


def update():
    global hovered, position, ammo_text
    if held_keys['a']:
        hovered.text = f'Hovered Entity : {mouse.hovered_entity}'
    else:
        hovered.text = ''
    if held_keys['e']:
        position.text = f'X : {controller.position[0]} Y : {controller.position[1]} Z : {controller.position[2]}'
    else:
        position.text = ''
    ammo_text.text = f'{current_weapon.magazine}/{current_weapon.ammo}'


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
    g18c = Weapon(ammo=54,
                  mag_size=10,
                  magazine=10,
                  reload_delay=1,
                  name='test',
                  model='gun_pistol',
                  parent=controller,
                  texture='grass',
                  collider='cube',
                  shoot_delay=.001,
                  mode='semi',
                  position=Vec3(0, 0, 0))

    current_weapon = g18c

    ammo_text = Text(text=f'{current_weapon.magazine}/{current_weapon.ammo}',
                     scale=3,
                     position=Vec3(.52, -.4, 0))

    app.run()