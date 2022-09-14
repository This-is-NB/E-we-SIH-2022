from PIL import Image
import os
num_key_frames = 8

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

with Image.open('face.gif') as im:
    num_key_frames = im.n_frames//1
    for i in range(num_key_frames):
        im.seek(im.n_frames // num_key_frames * i)
        im.save('frames/{}.png'.format(i)) 

# for frame_path in os.listdir('frames'):
#     frame = Image.open('frames/' +frame_path)
#     strip = Image.new('RGBA',(800,50),(48,105,162,255))


#     get_concat_v(strip,frame).save('frames/' +frame_path)