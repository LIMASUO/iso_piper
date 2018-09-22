# module to store the current plane and change it when required by the user

planes = ["xy", "yz", "zx"]
planes_dict = {0: planes[0], 1: planes[1], 2: planes[2]}
current_plane = 0
x_vec = (0.866, -0.5)
y_vec = (-0.866, -0.5)
z_vec = (0.0, 1.0)
dir_vec_map = {'x': x_vec, 'y': y_vec, 'z': z_vec}
planes_iterable = iter(planes_dict)


def set_current_plane(plane):
    global current_plane
    current_plane = plane
    print("current plane: " + str(planes_dict[plane]))


