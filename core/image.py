
"""
    core/image.py

    this module is responsible for:
        - image to PNG
        - image to ICO
        - image to STRING
        (useful stuff in working with images)

    author: @alexzander
"""


# python
import binascii
import optparse
import requests
import pytesseract

# 3rd party
import cv2
import pyzbar
import numpy as np # pip install numpy
from PIL import Image # pip install Pillow

# core package (pip install python-core)
from core.path__ import *
from core.system import *
from core.aesthetics import *
import core.exceptions
from core.download import download_file


# you need to set up in your environment variables TESS = { path your tesseract.exe file }
if "TESS" not in os.environ.keys():
    raise core.exceptions.NotFoundError("tesseract engine")
# pytesseract.pytesseract.tesseract_cmd = os.environ["TESS"]
pytesseract.pytesseract.tesseract_cmd = r"D:\Applications\tesseract_ocr\tesseract.exe"



from numba import jit, njit
# @jit
@jit(nopython=True)
def OverlayImage(src, overlay, pos=(0, 0), scale=1):
    # overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)

    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]    # Position of foreground/overlay image

    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = overlay[i][j][3] / 255.0
            src[x+i][y+j] = alpha*overlay[i][j][:3]+(1-alpha)*src[x+i][y+j]


class image_Exception(Exception):
    def __init__(self, message=""):
        self.message = message


class NotAnImageError(image_Exception):
    """ file is not an image """
    pass


def rgb_2_hex(red: int, green: int, blue: int):
    try:
        red = int(red)
        green = int(green)
        blue = int(blue)
    except:
        raise ValueError("@red, @green or @blue cannot be converted to integer")
    return "#{:02x}{:02x}{:02x}".format(red, green, blue)


def decode_qr_bar_code(path):
    """ return Decoded class """

    # validation
    if type(path) != str:
        path = str(path)
    if not is_file(path):
        raise NotAFileError
    # /validation

    img = cv2.imread(path)
    decoded = pyzbar.decode(img)
    return decoded


def hex_2_rgb(hexadecimal: int):
    if type(hexadecimal) != str:
        raise TypeError

    # starting from 1 -> meaning that is excluding the '#'
    return map(ord, hexadecimal[1:].decode("hex"))



def image_to_str_from_url(url):
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        response.raise_for_status()

    return pytesseract.image_to_string(Image.open(response.raw))


def image_to_str_from_file(path: str):
    """ return a string from image """
    return pytesseract.image_to_string(Image.open(path))


def image_to_str(location: str):
    if not isinstance(location, str):
        raise TypeError

    if location.startswith("http://") or location.startswith("https://"):
        return image_to_str_from_url(location)

    return image_to_str_from_file(location)


def save_pdf_from_image(path: str, dst_folder: str):
    """ saves pdf from image to dst specified by user """
    image_name = path.split("\\")[-1].split(".")[0]
    binary_pdf = pytesseract.image_to_pdf_or_hocr(Image.open(path))

    with open(dst_folder + "\\{}.pdf".format(image_name), "wb") as bin_file:
        bin_file.truncate(0)
        bin_file.write(binary_pdf)


def image_to_pdf(path: str):
    """ raw binary content of a pdf file from image file """
    return pytesseract.image_to_pdf_or_hocr(Image.open(path))


def image_to_png(path: str):
    path = get_path_from_absolute(path)
    filename = get_file_name(path)

    img = Image.open(path)
    img.save("{}/{}.png".format(path, filename))


def image_to_ico(path: str):
    img = Image.open(path)
    filename = get_file_name(path)
    path = get_path_from_absolute(path)
    img.save("{}/{}.ico".format(path, filename))

def save_gif(dst, images, fps=1):
    if type(images) != list:
        raise TypeError("param @images should be type list.")
    if type(dst) != str:
        raise TypeError("param @dst should be type str.")

    if not dst.endswith(".gif"):
        raise ValueError("param @destinaion should end with .gif extension.")

    import imageio
    images = [imageio.imread(image_abspath) for image_abspath in images]
    imageio.mimsave(dst, images, fps=fps)


def print_image(path):
    def get_ansi_color_code(r, g, b):
        if r == g and g == b:
            if r < 8:
                return 16
            if r > 248:
                return 231
            return round(((r - 8) / 247) * 24) + 232
        return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)


    def get_color(r, g, b):
        return "\x1b[48;5;{}m \x1b[0m".format(int(get_ansi_color_code(r,g,b)))

    img = Image.open(path)
    print(img.size)

    height = 80
    width = int((img.width / img.height) * height)

    img = img.resize((width, height), Image.ANTIALIAS)
    img_array = np.asarray(img)
    print(img_array.shape)

    for h_index in range(height):
        for w_index in range(width):
            pix = img_array[h_index][w_index]
            print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
        print()


def hide_text_in_image(path, text):
    image = Image.open(path)
    # tuples of 4 elements
    image_data = list(image.getdata())

    if len(image_data) * 3 < len(text) * 8:
        raise ValueError("message '{}'(len=={}) is  too big to insert in image".format(text, len(text)))
    else:
        color_index = 3
        pixel_index = 0

        for text_byte in bytearray(text, 'utf8'):
            for i in range(8):
                info = text_byte
                info &= 1 << i
                info >>= i

                pixel = list(image_data[pixel_index])
                pixel[color_index % 3] &= ~1
                pixel[color_index % 3] |= info
                image_data[pixel_index] = tuple(pixel)

                if color_index % 3 >= 2:
                    pixel_index += 1
                color_index += 1

        encoded_image = Image.new('RGB', image.size)
        encoded_image.putdata(image_data)

        image_name = get_file_name(path)

        encoded_image.save('{}_encoded.png'.format(image_name), format='PNG')
        encoded_image.close()

    image.close()

    # code=0
    return True


def reveal_text_from_image(path):
    image = Image.open(path)
    image_data = list(image.getdata())
    decoded_text = ''

    char = bytearray('\0', 'utf8')
    color_index = 3
    pixel_index = 0

    while pixel_index < 500:
        for bit_index in range(8):
            byte = image_data[pixel_index][color_index % 3]
            byte &= 1
            char[0] |= byte << bit_index

            if color_index % 3 >= 2:
                pixel_index += 1
            color_index += 1

        try:
            decoded_text += char.decode('utf8')
        except UnicodeDecodeError:
            pass
        char[0] &= 0

    return decoded_text


def __transposed_image(image, rotation):
    if isinstance(image, Image.Image):
        return image.transpose(rotation)

    elif isinstance(image, str):
        img = Image.open(image)
        return img.transpose(rotation)
    else:
        raise TypeError


# ========= by default is counter-clock wise =======

def rotated_90_image(image: Image.Image):
    return __transposed_image(image, Image.ROTATE_90)


def rotated_180_image(image: Image.Image):
    return __transposed_image(image, Image.ROTATE_180)


def rotated_270_image(image: Image.Image):
    return __transposed_image(image, Image.ROTATE_270)

# ========= by default is counter-clock wise =======


def flipped_left_to_right_image(image: Image.Image):
    return __transposed_image(image, Image.FLIP_LEFT_RIGHT)


def flipped_up_to_bottom_image(image: Image.Image):
    return __transposed_image(image, Image.FLIP_TOP_BOTTOM)






if __name__ == '__main__':
    # p = "D:/Alexzander__/programming/python/python.png"
    # names = [
    #     "90.png",
    #     "180.png",
    #     "270.png",
    #     "left_to_right.png",
    #     "up_to_bottom.png",
    # ]

    # funcs = [
    #     rotated_90_image,
    #     rotated_180_image,
    #     rotated_270_image,
    #     flipped_left_to_right_image,
    #     flipped_up_to_bottom_image
    # ]

    # for arg, func in zip(names, funcs):
    #     x = func(p)
    #     x.save(arg)
    # print(image_to_str("https://i.stack.imgur.com/g0YKh.png"))
    print(image_to_str("https://i.stack.imgur.com/aF598.png"))