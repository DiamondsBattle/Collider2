from ursina import *
from keybinds import keybind

class FirstPersonController(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.speed = 5

        self.cursor = Text(parent=camera.ui, text='+', scale=2)

        self.position = (0, 1, 1)
        camera.position = self.position
        camera.rotation = (0, 0, 0)
        camera.fov = 90
        mouse.locked = True
        self.mouse_sensitivity = Vec2(40, 40)
        self.target_smoothing = 100
        self.smoothing = self.target_smoothing

        self.grounded = False
        self.jump_height = 2
        self.jump_duration = .5
        self.jumping = False
        self.air_time = 0

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[1]
        camera.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0]
        camera.rotation_x = clamp(camera.rotation_x, -90, 90)

        self.direction = Vec3(
            self.forward * (held_keys[keybind['forward']] - held_keys[keybind['backward']])
            + self.right * (held_keys[keybind['left']] - held_keys[keybind['right']])
            ).normalized()

        self.smoothing = lerp(self.smoothing, self.target_smoothing, 4*time.dt)
        camera.position = lerp(
            camera.position,
            self.position + (self.up*1.5),
            self.smoothing / 100)

        camera.rotation_y = self.rotation_y

        origin = self.world_position + (self.up*.5) + (self.direction/2)
        middle_ray = raycast(origin, self.direction, ignore=[self,], distance=.25, debug=False)
        left_ray = raycast(origin, lerp(self.left, self.forward, .125), ignore=[self,], distance=1.4, debug=False)
        right_ray = raycast(origin, lerp(self.right, self.forward, .125), ignore=[self,], distance=1.4, debug=False)

        # push away from the wall
        # if left_ray.hit:
        #     self.smoothing = 2
        #     self.position -= lerp(self.left, self.forward, .5) * (1.399-left_ray.distance)
        #
        # elif right_ray.hit:
        #     self.smoothing = 2
        #     self.position -= lerp(self.right, self.forward, .5) * (1.399-right_ray.distance)

        if not middle_ray.hit:
            self.position += self.direction * self.speed * time.dt

        # gravity
        ray = boxcast(self.world_position+(0, .05, 0), self.down, ignore=(self, ), thickness=.9)

        if ray.distance <= .1:
            if not self.grounded:
                self.land()
            self.grounded = True
            # self.y = ray.world_point[1]
            return
        else:
            self.grounded = False

        # if not on ground and not on way up in jump, fall
        if not self.grounded:
            self.y -= min(self.air_time, ray.distance-.05)
            self.air_time += time.dt*.25

    def input(self, key):
        if key == keybind['jump']:
            self.jump()

    def jump(self):
        if not self.grounded:
            return

        self.grounded = False
        self.animate_y(self.y + self.jump_height, self.jump_duration, resolution=120, curve=curve.out_expo)
        for i in self.children:
            i.animate_y(i.y + self.jump_height, self.jump_duration, resolution=120, curve=curve.out_expo)
        invoke(self.start_fall, delay=self.jump_duration)

    def start_fall(self):
        self.y_animator.pause()
        self.jumping = False

    def land(self):
        # print('land')
        self.air_time = 0
        self.grounded = True