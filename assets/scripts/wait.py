from ursina import *
from threading import Thread
from time import sleep

def wait(delay):
    t = Thread(target=Func(sleep, delay))
    t.start()