

from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np





text_to_show = "Testing test"
monaco_font_path = r"D:\Alexzander__\fonts\monaco\monaco.ttf"

image = cv2.imread("background.png")


cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pil_im = Image.fromarray(cv2_im_rgb)

draw = ImageDraw.Draw(pil_im)
font = ImageFont.truetype(monaco_font_path, 50)

draw.text((100, 300), text_to_show, font=font, fill=(155, 155, 255))

cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)


cv2.namedWindow("window", cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('window', cv2_im_processed)
cv2.waitKey(0)
cv2.destroyAllWindows()