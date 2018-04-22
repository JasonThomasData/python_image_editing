import math

def update_category_max(category_max, category_min, category_size):
    return category_min + category_size

def get_size_of_categories(number_of_categories):
    return math.floor(255 / number_of_categories)

def get_category_median(category_min, category_size):
    return category_min + math.ceil(category_size / 2)

def create_category(category_max, category_min, category_size):
    category = {
        'min' : category_min,
        'max' : category_max,
        'median' : get_category_median(category_min, category_size)
    }
    return category

def update_category_min(category_max, category_min):
    return category_max + 1

def get_colour_categories(number_of_categories):
    colour_categories = []
    category_size = get_size_of_categories(number_of_categories)
    category_min = 0
    category_max = 0
    for _ in range(number_of_categories):
        category_max = update_category_max(category_max, category_min, category_size)
        category = create_category(category_max, category_min, category_size)
        colour_categories.append(category)
        category_min = update_category_min(category_max, category_min)
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
