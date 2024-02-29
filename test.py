from PIL import Image

def encode_lsb(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    encoded = img.copy()

    if len(message) * 3 > width * height:
        raise ValueError("Message is too long to encode in the image")

    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'

    index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(encoded.getpixel((x, y)))

            for i in range(3):
                if index < len(binary_message):
                    pixel[i] = pixel[i] & ~1 | int(binary_message[index])
                    index += 1

            encoded.putpixel((x, y), tuple(pixel))

    encoded.save("encoded_image.png")
    print("Image encoded successfully.")

def decode_lsb(image_path):
    encoded = Image.open(image_path)
    width, height = encoded.size

    binary_message = ''
    for y in range(height):
        for x in range(width):
            pixel = encoded.getpixel((x, y))
            for color in pixel[:3]:
                binary_message += str(color & 1)

    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if byte == '11111111':
            break
        message += chr(int(byte, 2))

    print("Decoded message:", message)

# Пример использования:
image_path = "fire_apple.jpg"
message = "Hello, this is a secret message!"

# Кодирование сообщения в изображение
encode_lsb(image_path, message)

# Декодирование сообщения из изображения
decode_lsb("encoded_image.png")
