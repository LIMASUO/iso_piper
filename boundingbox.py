# This module is responsible for creating the bounding box that would
# enclose the isometric drawing components. The bounding box will be
# used to verify whether a point lies within the bounds when creating
# new entities, and would allow resizing the entire pipeline if the
# addition of new components causes the entities to go beyond limits.

from tkinter import *
import constants
import geometry
import isoplane
import components

vertices = []   # hexagon vertices in anti-clockwise sequence starting center bottom
enabled = True


# Creates the hexagon for the isometric representation of the bounding box.
# This may need to be converted into a hexagon primitive type and added
# to the geometry module.

def initialize_boundingbox(canvas, curr_canvas_width=constants.DEFAULT_CANVAS_WIDTH,
                           curr_canvas_height=constants.DEFAULT_CANVAS_HEIGHT):
    global vertices
    global enabled
    enabled = True
    vertices = []
    v0 = [curr_canvas_width * 0.5,
          curr_canvas_height - constants.BBOX_VERT_MARGIN]
    slope_line_len = (curr_canvas_width * 0.5
                      - constants.BBOX_RIGHT_MARGIN) / constants.COS_30
    v1 = geometry.translate_along_vector(v0, isoplane.y_vec, slope_line_len)
    v5 = geometry.translate_along_vector(v0, isoplane.x_vec, slope_line_len)
    components.line(canvas, v0[0], v0[1], constants.BBOX_COLOR, 'bbox_line1', 'x',
                    slope_line_len)
    components.line(canvas, v0[0], v0[1], constants.BBOX_COLOR, 'bbox_line6', 'y',
                    slope_line_len)
    v3 = [curr_canvas_width * 0.5, constants.BBOX_VERT_MARGIN]
    v2 = geometry.translate_along_vector(v3, isoplane.y_vec_inv, slope_line_len)
    components.line(canvas, v3[0], v3[1], constants.BBOX_COLOR, 'bbox_line3', 'x',
                    -slope_line_len)
    v4 = geometry.translate_along_vector(v3, isoplane.x_vec_inv, slope_line_len)
    components.line(canvas, v3[0], v3[1], constants.BBOX_COLOR, 'bbox_line4', 'y',
                    -slope_line_len)
    canvas.create_line(v1[0], v1[1], v2[0], v2[1], fill=constants.BBOX_COLOR,
                       tags="bbox_line2")
    canvas.create_line(v4[0], v4[1], v5[0], v5[1], fill=constants.BBOX_COLOR,
                       tags="bbox_line5")
    vertices.append(v0)
    vertices.append(v1)
    vertices.append(v2)
    vertices.append(v3)
    vertices.append(v4)
    vertices.append(v5)
    count = 0
    for vertex in vertices:
        canvas.delete("bbox_circle" + str(count + 1))
        canvas.create_oval(vertex[0] + 2, vertex[1] + 2, vertex[0] - 2,
                           vertex[1] - 2, outline=constants.BBOX_COLOR,
                           fill=constants.BBOX_COLOR, width=2,
                           tags="bbox_circle" + str(count + 1))
        count += 1


def clear_boundingbox(canvas):
    global enabled
    line_test = canvas.find_withtag("bbox_line1")
    if line_test:
        for i in range(0, 6):
            canvas.delete("bbox_line" + str(i + 1))
    circle_test = canvas.find_withtag("bbox_circle1")
    if canvas.winfo_height() != 1:
        if circle_test:
            for i in range(0, 6):
                canvas.delete("bbox_circle" + str(i + 1))
    enabled = False


def draw_boundingbox(canvas, curr_canvas_width, curr_canvas_height):
    if enabled:
        if canvas.winfo_height() == 1:
            initialize_boundingbox(canvas)
        else:
            clear_boundingbox(canvas)
            initialize_boundingbox(canvas, curr_canvas_width, curr_canvas_height)


def toggle_boundingbox(canvas):
    global enabled
    if enabled:
        clear_boundingbox(canvas)
    else:
        enabled = True
        draw_boundingbox(canvas, canvas.winfo_width(), canvas.winfo_height())

