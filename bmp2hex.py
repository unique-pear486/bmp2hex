import sys
import io
from PIL import Image


def img2bin(filepath):
    """
    Convert image to byte array
    """
    img = Image.open(filepath)

    # Check that the input image is correctly formatted
    if img.size != (128, 64):
        raise Exception("Image wrong size\nMust be 128x64px")
    if img.mode != '1':
        raise Exception("Image wrong mode\nMust be 1-bit (monochrome")

    # place the bytes in the byte array
    image = bytearray()
    for row in range(0, 8):
        for col in range(0, 128):
            byte = 0
            for i in range(0, 8):
                x = col
                y = row * 8 + i
                bit = int(not img.getpixel((x, y)))     # 0=light on
                byte = byte + 2**i * bit
            image.append(byte)
    return image


if __name__ == "__main__":
    img = img2bin(sys.argv[1])
    with io.open(sys.argv[2], "wb") as f:
        f.write(img)
