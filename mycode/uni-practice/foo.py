def pixel_to_comp(z: complex, w: complex, x: int, y: int, rx: int, ry: int) -> complex:
    """Return complex number assoc with a specific pixel value given x by y."""

    axis_x = rx / 2
    axis_y = rx / 2
    new_x_coor = x - axis_x
    new_y_coor = y - axis_y

    xn = new_x_coor/axis_x
    yn = new_x_coor/axis_y

    mycomplex = complex(xn, yn)
    return mycomplex


z = complex(-1, -1)
w = complex(1, 1)
height = 8
width = 8
