def get_colour_categories(number_of_categories):
    if number_of_categories == 2:
        colour_categories = [
            {
                'min' : 0,
                'max' : 127,
                'median' : 64
            },
            {
                'min' : 128,
                'max' : 255,
                'median' : 192
            }
        ]
    elif number_of_categories == 3:
        colour_categories = [
            {
                'min' : 0,
                'max' : 84,
                'median' : 42
            },
            {
                'min' : 85,
                'max' : 170,
                'median' : 127
            },
            {
                'min' : 171,
                'max' : 255,
                'median' : 213
            }
        ]
    elif number_of_categories == 4:
        colour_categories = [
            {
                'min' : 0,
                'max' : 63,
                'median' : 32
            },
            {
                'min' : 64,
                'max' : 127,
                'median' : 96
            },
            {
                'min' : 128,
                'max' : 191,
                'median' : 150
            },
            {
                'min' : 192,
                'max' : 255,
                'median' : 222
            }
        ]

    return colour_categories 

def get_categories(red_category_number, green_category_number, blue_category_number):
    min_limit = 0
    max_limit = 255
    rgb_categories = {
        'red' : get_colour_categories(red_category_number),
        'green' : get_colour_categories(green_category_number),
        'blue' : get_colour_categories(blue_category_number)
    }
    return rgb_categories
