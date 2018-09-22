# This module will house the geometry related utilities required for the
# creation, transformation, and positioning of components (engineering,
# and non-engineering).


def translate_along_vector(point, vec, length):
    new_point = [point[0] + length * vec[0], point[1] + length * vec[1]]
    return new_point


def apply_isometric_reduction(len):
    pass
