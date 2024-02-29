from PIL import Image
from math import ceil
# таск 2 генератор псевдослучайныйх чисел
PATH = 'fire_apple.jpg'
MESSAGE = 'Apple'
BIN_MESSAGE = ''.join(format(ord(sim), '08b') for sim in MESSAGE) + '1111111111111110'
print(BIN_MESSAGE)

def read_img(path:str):
    return Image.open(path)

def get_pixels(img):
    return img.load()

def encode():
    img = Image.open('fire_apple.jpg')
    width, height = img.size
    tmp = img.copy()

    index = 0
    for y in range(height):
        for x in range(width): 
            if index >= len(BIN_MESSAGE):
                    break
            pixel = list(tmp.getpixel((x, y)))
            for i in range(3):
                if index < len(BIN_MESSAGE):
                    pixel[i] = pixel[i] & ~1 | int(BIN_MESSAGE[index])
                    index += 1
            tmp.putpixel((x,y),tuple(pixel))
    tmp.save('encoded_image.png')
    print('Code complete successful')

def decode():
    img = Image.open('encoded_image.png')
    message = ''
    width, height = img.size
    binary_message = ''

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x,y))
            for channel in pixel:
                binary_message += str(int(channel % 2))
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        message += chr(int(byte, 2))

    print(message[0:32])

def main():
    encode()
    decode()

if __name__ == "__main__":
    main()