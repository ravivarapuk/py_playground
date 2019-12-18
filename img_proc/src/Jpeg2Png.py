import sys
import os
from PIL import Image

img_folder = sys.argv[1]
op_folder = sys.argv[2]


def jpg2png(a, b):
    if not os.path.exists(b):
        os.makedirs(b)

    for filename in os.listdir(a):
        img = Image.open(f'{a}/{filename}')
        name = os.path.splitext()[0]
        img.save(f'{b}/{name}.png', 'png')
    
    return 'all done!'


# Run Module
print(jpg2png(img_folder, op_folder))