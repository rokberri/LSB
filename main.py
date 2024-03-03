from PIL import Image
from math import ceil,fmod
from time import time



# Квадратичный конгруэнтный генератор
def lin_rand_arr_flxd(seed,max_el,size):
    a=47
    b=12345
    if size == 1:
        return ceil(fmod(a*ceil(seed)+b,max_el))
    r = [0 for i in range(size)]
    r[0] = ceil(seed)
    for i in range(1,size):
        r[i] = ceil(fmod((a*r[i-1]+b),max_el))
    return r[1:size]
# ------------------------------------

PATH = 'fire_apple.jpg'
MESSAGE = 'Apple'
BIN_MESSAGE = ''.join(format(ord(sim), '08b') for sim in MESSAGE) + '11111111'
SEED = time()


def read_img(path:str):
    return Image.open(path)

def get_pixels(img):
    return img.load()

def encode():
    img = Image.open('fire_apple.jpg')
    width, height = img.size
    tmp = img.copy()
    ref_img = img.copy()

    index = 0
    pixels_height = lin_rand_arr_flxd(SEED, height, height-1)
    pixels_width = lin_rand_arr_flxd(SEED, width,width-1)

    for y in pixels_height:
        for x in pixels_width: 
            if index >= len(BIN_MESSAGE):
                    break
            pixel = list(tmp.getpixel((x, y)))
            for i in range(3):
                if index < len(BIN_MESSAGE):
                    pixel[i] = pixel[i] & ~1 | int(BIN_MESSAGE[index])
                    index += 1
            ref_img.putpixel((x,y), tuple([0,0,255]))        
            tmp.putpixel((x,y),tuple(pixel))
    ref_img.save('ref_img.png')
    tmp.save('encoded_image.png')

def decode():
    img = Image.open('encoded_image.png')
    message = ''
    width, height = img.size
    binary_message = ''
    
    pixels_height = lin_rand_arr_flxd(SEED, height, height-1)
    pixels_width = lin_rand_arr_flxd(SEED, width,width-1)


    for y in pixels_height:
        for x in pixels_width: 
            pixel = img.getpixel((x,y))
            for channel in pixel:
                binary_message += str(int(channel % 2))
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if byte == '11111111':
            break
        message += chr(int(byte, 2))

    print(message[0:32])

def main():
    encode()
    decode()

if __name__ == "__main__":
    main()