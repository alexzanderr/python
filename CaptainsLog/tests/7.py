


from PIL import Image, ImageTk
import cv2
import tkinter
from pathlib import Path
from time import sleep
from functools import partial

root = tkinter.Tk()


background_image_path = Path("background.png")
monster_image_path = Path("monster.png")


def load_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)

    return ImageTk.PhotoImage(image)

# images = [
#     load_image(img_path) for img_path in [background_image_path, monster_image_path]
# ]

background_image = load_image(background_image_path.as_posix())
monster_image = load_image(monster_image_path.as_posix())



image_label = tkinter.Label(root, image=background_image)
image_label.image = background_image
image_label.pack()

used = True

def change_image():
    global used
    # for _ in range(50):
    if used:
        image_label.configure(image=background_image)
        used = False
    else:
        image_label.configure(image=monster_image)
        used = True


button = tkinter.Button(root, text="press", command=change_image)
button.pack()

root.mainloop()