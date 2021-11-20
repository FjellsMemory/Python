def sample(z: complex, w: complex, x: int, y: int, rx: int, ry: int) -> complex:
    """Return complex number assoc with a specific pixel value on grid x, y.
    scale = rx / ry
    axis_x = rx / 2 #* (abs(z.real) - abs(w.real))
    axis_y = ry / 2 #* (abs(z.imag) - abs(w.real))
    new_x_coor = x - axis_x
    new_y_coor = y - axis_y

    ratio_x = (x) / rx
    ratio_y = (y) / ry
    final_x = ratio_x * (z.real + w.real)
    final_y = ratio_y * (z.imag + w.imag)

    xn = new_x_coor / axis_x#/ (abs(z.real) + abs(w.real))
    yn = new_y_coor / axis_y#/ (abs(z.imag) + abs(w.imag))

    mycomplex = complex(final_x, final_y)
    return mycomplex
    """

z = complex(-1, -1)
w = complex(1, 1)
height = 8
width = 8
