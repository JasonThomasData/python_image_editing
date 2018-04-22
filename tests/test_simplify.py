import pytest
import application.simplify

categories = {
    'red': [
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
    ],
    'green': [
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
    ],
    'blue': [
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
}

def test_simplify_colour_54_to_64():
    red_value = 54
    simple_colour = application.simplify.simplify_colour(red_value, categories['red'])
    assert simple_colour == 64

def test_simplify_colour_211_to_192():
    red_value = 211
    simple_colour = application.simplify.simplify_colour(red_value, categories['red'])
    assert simple_colour == 192

def test_simplify_colour_128_to_192():
    red_value = 128
    simple_colour = application.simplify.simplify_colour(red_value, categories['red'])
    assert simple_colour == 192

def test_simplify_pixel_12_78_239_to_64_64_192():
    pixel = (12, 78, 239)
    simple_pixel = application.simplify.simplify_pixel(pixel, categories)
    assert simple_pixel == (64, 64, 192)
