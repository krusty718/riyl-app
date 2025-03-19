import PIL.Image

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image):
    return image.resize((75,37))

def to_grayscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str


def main():
    image = PIL.Image.open('logo.png')

    image = resize_image(image)
    grayscale_image = to_grayscale(image)
    ascii_str = pixel_to_ascii(grayscale_image)
    img_width = grayscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    
    print(ascii_img)
    print(f'\t\t\tRIYL-App\n\t\t\tIlya Zinger, 2024\n\n')

if __name__ == "__main__":
    main()
