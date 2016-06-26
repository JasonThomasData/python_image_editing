import math
from PIL import Image

def get_numbers_of_squares(image_width, image_height, square_width):
    square_number_wide = int(math.floor(image_width / square_width))
    square_number_high = int(math.floor(image_height / square_width))
    return square_number_wide, square_number_high

def get_square_pixel_dimension_w(s_w, square_width):
    square_starting_w = s_w * square_width
    square_ending_w = square_starting_w + square_width
    return square_starting_w, square_ending_w

def get_square_pixel_dimension_h(s_h, square_height):
    square_starting_h = s_h * square_height
    square_ending_h = square_starting_h + square_height
    return square_starting_h, square_ending_h

def draw_new_square(new_image_data, square_starting_w, square_ending_w, square_starting_h, square_ending_h, average_color_of_square):
    for pix_w in range(square_starting_w, square_ending_w):
        for pix_h in range(square_starting_h, square_ending_h):
            new_image_data.putpixel((pix_w, pix_h), average_color_of_square)
    return new_image_data

def get_square_average_colour(image_data, square_starting_w, square_ending_w, square_starting_h, square_ending_h, square_width):
    total_r, total_g, total_b = 0, 0, 0
    pixel_number = square_width * square_width
    for pix_w in range(square_starting_w, square_ending_w):
        for pix_h in range(square_starting_h, square_ending_h):
            pix_r, pix_g, pix_b = image_data[pix_w, pix_h]
            total_r += pix_r
            total_g += pix_g
            total_b += pix_b
    average_r = total_r / pixel_number
    average_g = total_g / pixel_number
    average_b = total_b / pixel_number
    return (average_r, average_g, average_b)

def process_image_data(image_data, image_width, image_height, square_width):
    square_number_wide, square_number_high = get_numbers_of_squares(image_width, image_height, square_width)
    new_image_data = Image.new('RGB', (image_width, image_height), 'white')
    for s_w in range(square_number_wide):
        for s_h in range(square_number_high):
            square_starting_w, square_ending_w = get_square_pixel_dimension_w(s_w, square_width)
            square_starting_h, square_ending_h = get_square_pixel_dimension_h(s_h, square_width)
            average_color_of_square = get_square_average_colour(image_data, square_starting_w, square_ending_w, square_starting_h, square_ending_h, square_width)
            new_image_data = draw_new_square(new_image_data, square_starting_w, square_ending_w, square_starting_h, square_ending_h, average_color_of_square)
    return new_image_data