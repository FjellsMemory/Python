# dg239
"""Paint the Mandelbrot set on a canvas."""
from PIL import Image


def mandelbrot(c: complex, m: int) -> int:
    """
    Membership test for Mandelbrot set given m number of iterations.

    Input complex number and number of iterations to perform mandelbrot formula
    on; return the index value i if zsubi ever becomes larger than 2.  If it
    never does, just return m.
    """
    index = 1  # what iteration we're on
    current_sum = c  # current sum
    max_iterations = m
    while index < max_iterations:
        if abs(current_sum) >= 2:
            return index
        else:
            current_sum = (current_sum ** 2) + c
        index += 1
    return m


def sample(z: complex, w: complex, x: int, y: int, rx: int, ry: int) -> complex:
    """Return complex number assoc with a specific pixel value on grid x, y."""
    final_x = ((x / rx) * abs(z.real - w.real)) + z.real
    final_y = ((y / ry) * abs(z.imag - w.imag)) + z.imag
    mycomplex = complex(final_x, final_y)
    return mycomplex


def color(i: int, max_i: int) -> tuple[int, int, int]:
    """Give a pixel a color based on its successful number of loops."""
    # Farbton in Abhängigkeit der benötigten Schleifendurchläufe.
    hue = int(255 * (i / max_i))
    # Volle Helligkeit 255, außer wenn c Teil der Mandelbrotmenge ist.
    # Dadurch wird das innere schwarz.
    value = 255 if i < max_i else 0
    # Volle Sättigung
    saturation = 255
    return (hue, saturation, value)


def render_mandelbrot(
    z: complex, w: complex,      # Intervall auf der komplexen Ebene.
    width: int, height: int,     # Auflösung des zu erzeugenden Bildes.
    max_loops: int,              # Anzahl maximaler Schleifendurchläufe.
    name: str                    # Dateiname des zu erzeugenden Bildes.
):
    """Take complex interval params, canvas params, loops, make M-brot.jpg."""
    # Erstelle ein Bild mit Auflösung 800x600 wobei die einzelnen
    # Pixel das HSV-Farbformat verwenden (Hue-Saturation-Value).
    size = (width, height)
    img = Image.new('HSV', size)
    # Setze die Farbe von jedem Pixel auf rot.
    for x in range(size[0]):
        for y in range(size[1]):
            # Bei Interesse siehe HSV-Farbraum auf Wikipedia.
            # Sie müssen für die Aufgabe nicht verstehen, wieso
            # folgendes Tupel der Farbe Rot entspricht.
            mycompnum = sample(z, w,
                               x, y, width, height)
            my_success_loops = mandelbrot(mycompnum, max_loops)
            my_color = color(my_success_loops, max_loops)
            img.putpixel((x, y), my_color)
    # Speichere das Bild als JPEG-Datei im aktuellen Verzeichnis.
    # Wir konvertieren das HSV-Farbformat zu RGB (Red-Green-Blue),
    # da JPEG kein HSV unterstützt.
    img.convert('RGB').save(name, quality=95)


if __name__ == "__main__":
    assert mandelbrot(0.5, 50) == 5
    assert mandelbrot(0.5, 4) == 4
    render_mandelbrot(-0.58 + 0.65j, -0.55 + 0.68j, 1000, 1000, 50, 'mandel1.jpg')
