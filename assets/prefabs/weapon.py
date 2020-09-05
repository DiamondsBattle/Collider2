from ursina import *
from keybinds import keybind

class Weapon(Entity):
    def __init__(self, name, ammo, shoot_delay, mode, magazine, reload_delay, mag_size, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.ammo = ammo
        self.mag_size = mag_size
        self.magazine = magazine
        self.shoot_delay = shoot_delay
        self.mode = mode
        self.reload_delay = reload_delay
        self.reloading = False
        self.can_shoot = True
        self.bullets = []

    def update(self):
        if held_keys['left mouse'] and self.mode == 'auto' and self.can_shoot:
            self.shoot()
            self.can_shoot = False
            if not self.reloading:
                invoke(setattr, self, 'can_shoot', True, delay=self.shoot_delay)

    def input(self, key):
        if key == 'left mouse down' and self.mode == 'semi' and self.can_shoot:
            self.shoot()
            self.can_shoot = False
            if not self.reloading:
                invoke(setattr, self, 'can_shoot', True, delay=self.shoot_delay)
        if key == keybind['gun_reload']:
            self.can_shoot = False
            self.reloading = True
            invoke(function=self.reload, delay=self.reload_delay)

    def magazineIsEmpty(self):
        if self.magazine <= 0:
            return True
        else:
            return False

    def shoot(self):
        if self.magazine == 1:
            self.magazine -= 1
            self.can_shoot = False
            self.reloading = True
            invoke(self.reload, delay=self.reload_delay)
        elif not self.magazineIsEmpty():
            self.magazine -= 1
        elif self.magazine <= 0:
            self.can_shoot = False
            self.reloading = True
            invoke(self.reload, delay=self.reload_delay)

    def reload(self):
        self.can_shoot = False
        self.reloading = True
        if self.mag_size <= self.ammo:
            self.magazine += self.mag_size
            if self.magazine > self.mag_size:
                old_mag = self.magazine
                self.magazine = self.mag_size
                self.ammo += old_mag - self.magazine
            self.ammo -= self.mag_size
        elif self.mag_size > self.ammo:
            old_ammo = self.ammo
            self.magazine += self.ammo
            self.ammo -= old_ammo
        self.can_shoot = True
        self.reloading = False