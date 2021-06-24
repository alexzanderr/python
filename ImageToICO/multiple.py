

from ImageToICO import ConvertImage
from pathlib import Path


image_path = "/home/alexzander/Alexzander__/programming/python/202020_order/assets/icons/appicon.png"
image = Path(image_path)


sizes_values = [
    (255, 255),
    (128, 128),
    (64, 64),
    (48, 48),
    (32, 32),
    (24, 24),
    (16, 16)
]


for size in sizes_values:
    result = ConvertImage(image, size)
    print(result)