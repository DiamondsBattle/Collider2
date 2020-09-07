from ursina import *

class Map(Entity):
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name