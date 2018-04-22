#!/usr/bin/env python3

import sys
from application import handle_file, simplify, rgb
from PIL import Image

def run_application():

    message = '''You must pass a file name and three integer values, like:
    `./make_simple FILENAME 2 3 4`'''
    try:
        assert len(sys.argv) == 5
        original_file_name = sys.argv[1]
        red_category_number = int(sys.argv[2])
        green_category_number = int(sys.argv[3])
        blue_category_number = int(sys.argv[4])
    except AssertionError:
        print(message)
        sys.exit()
    except TypeError:
        print(message)
        sys.exit()

    image_data, image_width, image_height = handle_file.load_file(original_file_name)

    rgb_categories = rgb.get_categories(red_category_number,green_category_number, blue_category_number)

    new_image_data = simplify.process_image_data(image_data, image_width, image_height, rgb_categories)

    rgb_string = '{}_{}_{}'.format(red_category_number, green_category_number, blue_category_number)

    handle_file.save_new_file(original_file_name, 'make_simple', rgb_string, new_image_data)

run_application()
