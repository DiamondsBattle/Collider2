from ursina import *
from keybinds import keybind
from assets.scripts.wait import wait
from threading import Thread
from time import sleep

class Weapon(Entity):
    def __init__(self, name, capacity, delay, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.capacity = capacity
        self.magazine = self.capacity
        self.delay = delay
        self.ammo_text = Text(text=f'{self.magazine}/{self.capacity}')
        self.bullets = []

    def update(self):
        self.ammo_text.text = f'{self.magazine}/{self.capacity}'
        if held_keys['left mouse']:
            self.shoot()
            wait(self.delay)

    def getName(self):
        return self.name

    def getCapacity(self):
        return self.capacity

    def canShoot(self):
        if self.magazine > 0:
            return True
        else:
            return False

    def shoot(self):
        if self.canShoot():
            self.magazine -= 1
        elif self.magazine == 0:
            invoke(self.reload, delay=2)

    def reload(self):
        self.magazine = self.capacity