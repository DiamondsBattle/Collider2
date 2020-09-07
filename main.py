from ursina import *
from assets.prefabs.controller import FirstPersonController
from assets.prefabs.weapon import Weapon
from assets.prefabs.map import Map
from keybinds import keybind
from ursina.shaders.basic_lighting import basic_lighting_shader


def update():
    global ammo_text, current_weapon_text, pickup_text

    try:
        ammo_text.text = f'{current_weapon.magazine}/{current_weapon.ammo}'
        current_weapon_text.text = f'{current_weapon.name} ({current_weapon.mode})'
        if current_weapon.parent != controller:
            current_weapon.parent = controller
    except Exception:
        ammo_text.text = ''
        current_weapon_text.text = ''


def input(key):
    global current_weapon
    if key == keybind['gun_change_mode'] and current_weapon:
        current_weapon.mode = 'semi' if current_weapon.mode == 'auto' else 'auto'
    if key == keybind['drop'] and current_weapon:
        current_weapon.parent = scene
        current_weapon = None


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
    m9 = Weapon(ammo=54,
                mag_size=15,
                magazine=15,
                reload_delay=2,
                name='M9',
                model='m9',
                collider='box',
                shoot_delay=.2,
                mode='semi',
                position=Vec3(0, 0, 0),
                scale=.2,
                shader=basic_lighting_shader)
    scar_l = Weapon(ammo=360,
                    mag_size=30,
                    magazine=30,
                    reload_delay=3,
                    name='Scar-L',
                    model='scar_l',
                    collider='box',
                    shoot_delay=.08,
                    mode='auto',
                    position=Vec3(0, 0, 0),
                    scale=.01,
                    shader=basic_lighting_shader)

    map = Map(name='bureau',
              # model='building',
              shader=basic_lighting_shader,
              collider='none',
              y=6)

    current_weapon = scar_l
    current_weapon.parent = controller
    current_weapon.position = Vec3(.8, 1.2, 1.5)
    current_weapon.rotation = Vec3(0, -180, 0) if current_weapon == scar_l else current_weapon.rotation

    ammo_text = Text(text=f'{current_weapon.magazine}/{current_weapon.ammo}',
                     scale=3,
                     position=Vec3(.52, -.4, 0))
    current_weapon_text = Text(text=f'{current_weapon.name} ({current_weapon.mode})',
                               position=Vec3(.53, -.3, 0))
    pickup_text = Text(text='',
                       position=Vec3(.54, -.2, 0))

    app.run()
