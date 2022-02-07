# mv237, lm599
from PIL import Image


def mandelbrot(c: complex, m: int) -> int:
    z = 0.0
    count = 0
    while abs(z) < 2 and count <= m:
        z = z**2 + c
        count += 1
    return count if abs(z) >= 2 and count <= m else m


def sample(z: complex, w: complex, x: int,
           y: int, sx: int, sy: int) -> complex:
    c1 = z.real + (abs(z.real) + abs(w.real)) * (x / sx)
    c2 = z.imag + (abs(z.imag) + abs(w.imag)) * (y / sy)
    return complex(c1, c2)


def color(i: int, max_i: int) -> (int, int, int):
    hue = int(255 * (i / max_i))
    value = 255 if i < max_i else 0
    saturation = 255
    return (hue, saturation, value)


def render_mandelbrot(z: complex, w: complex,
                      sx: int, sy: int,
                      m: int,
                      name: str):
    size = (sx, sy)
    img = Image.new('HSV', size)
    for x in range(size[0]):
        for y in range(size[1]):
            color_value = color(mandelbrot(sample(z, w, x, y, sx, sy), m), m)
            img.putpixel((x, y), color_value)
    img.convert('RGB').save(name, quality=95)
    return


if __name__ == "__main__":
    assert mandelbrot(0.5, 50) == 5
    assert mandelbrot(0.5, 4) == 4

    render_mandelbrot(-0.7 + 0.6j, -0.5 + 0.7j, 900, 600, 50, 'markmandel1.jpg')
