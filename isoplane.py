# module to store the current plane and change it when required
# by the user

from tkinter import *

planes = ["XY", "YZ", "ZX"]
planes_dict = {0: planes[0], 1: planes[1], 2: planes[2]}
current_plane = 0


def set_current_plane(plane):
    global current_plane
    current_plane = plane
    print("current plane: " + str(planes_dict[plane]))


def draw_isoplane(canvas):
    global current_plane
    # canvas.create_line(4, 4, 50, 50, fill="red")