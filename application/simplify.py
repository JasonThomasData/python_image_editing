import math
from PIL import Image

def simplify_colour(colour, categories):
    for category in categories:
        if colour >= category["min"] and colour <= category["max"]:
            return category["median"]

def simplify_pixel(original_pixel, rgb_categories):
    red = original_pixel[0]
    green = original_pixel[1]
    blue = original_pixel[2]

    simple_red = simplify_colour(red, rgb_categories["red"])
    simple_green = simplify_colour(green, rgb_categories["green"])
    simple_blue = simplify_colour(blue, rgb_categories["blue"])

    return (simple_red, simple_green, simple_blue)

def process_image_data(image_data, image_width, image_height, rgb_categories):
    new_image_data = Image.new('RGB', (image_width, image_height), 'white')
    for pix_w in range(image_width):
        for pix_h in range(image_height):
            original_pixel = image_data[pix_w, pix_h]
            simple_pixel = simplify_pixel(original_pixel, rgb_categories) 
            new_image_data.putpixel((pix_w, pix_h), simple_pixel)

    return new_image_data
