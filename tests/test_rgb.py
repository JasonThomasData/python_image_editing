import pytest
import application.rgb

def test_get_colour_categories_2():
    colour_categories = application.rgb.get_colour_categories(2)

    assert colour_categories[0]['min'] == 0
    assert colour_categories[0]['max'] == 127
    assert colour_categories[0]['median'] == 64

    assert colour_categories[1]['min'] == 128
    assert colour_categories[1]['max'] == 255
    assert colour_categories[1]['median'] == 192 

def test_get_colour_categories_4():
    colour_categories = application.rgb.get_colour_categories(4)

    assert colour_categories[0]['min'] == 0
    assert colour_categories[0]['max'] == 63
    assert colour_categories[0]['median'] == 32

    assert colour_categories[1]['min'] == 64 
    assert colour_categories[1]['max'] == 127
    assert colour_categories[1]['median'] == 96

    assert colour_categories[2]['min'] == 128 
    assert colour_categories[2]['max'] == 191
    assert colour_categories[2]['median'] == 160

    assert colour_categories[3]['min'] == 192
    assert colour_categories[3]['max'] == 255
    assert colour_categories[3]['median'] == 224

