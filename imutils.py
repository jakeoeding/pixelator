from PIL import Image

def load_image(img_path):
    img = Image.open(img_path)
    img.load()
    return img

def resize_block_multiples(img, block_width, block_height):
    img_w, img_h = img.size
    desired_width = img_w // block_width * block_width
    desired_height = img_h // block_height * block_height
    return img.resize((desired_width, desired_height))

def save_image(im_arr, output_name):
    img = Image.fromarray(im_arr)
    img.save(output_name)