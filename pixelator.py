import numpy as np
import imutils

class Pixelator:
    def __init__(self, block_width, block_height, method='mean'):
        self.w = block_width
        self.h = block_height
        if method not in ['max', 'mean']:
            raise ValueError('method must be one of: max, mean')
        self.method = max if method == 'max' else lambda x: sum(x) / len(x)

    def load_image(self, img_name):
        img = imutils.load_image(img_name)
        img = imutils.resize_block_multiples(img, self.w, self.h)
        return np.asarray(img)

    def process(self, input_img, output_img):
        im_arr = self.load_image(input_img)
        h, w, c = im_arr.shape
        for k in range(c):
            for j in range(0, h, self.h):
                for i in range(0, w, self.w):
                    block_value = self.method(im_arr[j:j + self.h, i:i + self.w, k].flatten())
                    im_arr[j:j + self.h, i:i + self.w, k] = block_value
        imutils.save_image(im_arr, output_img)

if __name__ == '__main__':
    Pixelator(12, 12, 'mean').process('img/mountain.jpg', 'mountain-1.jpg')