from ursina import *
from assets.prefabs.controller import FirstPersonController
from assets.prefabs.weapon import Weapon
from keybinds import keybind


def update():
    global ammo_text, current_weapon_text

    ammo_text.text = f'{current_weapon.magazine}/{current_weapon.ammo}'
    current_weapon_text.text = f'{current_weapon.name} ({current_weapon.mode})'

def input(key):
    if key == keybind['gun_change_mode']:
        current_weapon.mode = 'semi' if current_weapon.mode == 'auto' else 'auto'


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
                  name='M9',
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
    current_weapon_text = Text(text=f'{current_weapon.name} ({current_weapon.mode})',
                               position=Vec3(.53, -.3, 0))

    app.run()