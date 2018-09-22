# module to draw objects on the canvas

import constants
import geometry
import isoplane


# draw a straight line in either of the 3 directions
# direction : this can be eithe x, y, or z
# x0 : the x component of the start point of the line
# y0 : the y component of the start point of the line
# line_length : optional length of the line relative to the bounding box
#               if not provided, length will be automatically adjusted
#               based on limits of the box to fit the entire set of graphics
# angle : the angle of the line relative to the current plane
def line(canvas, x0, y0, color, line_tag, direction='', line_length=0, angle=0):
    second_point = geometry.translate_along_vector([x0, y0],
                                                   isoplane.dir_vec_map[direction],
                                                   line_length)
    line_item = canvas.create_line(x0, y0, second_point[0], second_point[1],
                                   fill=color, tags=line_tag)
    return line_item


def highlight_current_isoplane(canvas):
    pass


def initialize_isoplane(canvas):
    base_pt = [constants.LEFT_PADDING, 525 - constants.BOTTOM_PADDING]
    canvas.create_line(base_pt[0], base_pt[1],
                       constants.LEFT_PADDING, 525 - constants.BOTTOM_PADDING
                       - constants.TRIAD_LEN, fill="red", tags="triadlinez")
    line(canvas, base_pt[0], base_pt[1], 'green3', "triadlinex", 'x',
         constants.TRIAD_LEN)
    line(canvas, base_pt[0], base_pt[1], 'gold2', "triadliney", 'y',
         constants.TRIAD_LEN)


def draw_isoplane(canvas):
    base_pt = [constants.LEFT_PADDING, canvas.winfo_height()
               - constants.BOTTOM_PADDING]
    if canvas.winfo_height() == 1:
        initialize_isoplane(canvas)
    else:
        z_line = canvas.find_withtag("triadlinez")
        if z_line:
            canvas.delete("triadlinez")
            canvas.create_line(base_pt[0], base_pt[1], constants.LEFT_PADDING,
                               canvas.winfo_height() - constants.BOTTOM_PADDING
                               - constants.TRIAD_LEN, fill="red", tags="triadlinez")
        x_line = canvas.find_withtag("triadlinex")
        if x_line:
            canvas.delete("triadlinex")
            line(canvas, base_pt[0], base_pt[1], 'green3', "triadlinex", 'x',
                 constants.TRIAD_LEN)
        y_line = canvas.find_withtag("triadliney")
        if y_line:
            canvas.delete("triadliney")
            line(canvas, base_pt[0], base_pt[1], 'gold2', "triadliney", 'y',
                 constants.TRIAD_LEN)


class Ports:
    def __init__(self):
        self.coords = []


class Pipe:
    def __init(self):
        pass


class Elbow:
    def __init__(self):
        pass


class Tee:
    def __init__(self):
        pass

