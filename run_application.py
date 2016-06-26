import sys
from application import handle_file, mosaic
from PIL import Image

def run_application():
    if len(sys.argv) == 4:
        original_file_name = sys.argv[1]
        process_name = sys.argv[2]
        square_width = int(sys.argv[3])
    else:
        print 'Need at least two arguments, eg. `python run_application.py original.jpg mosaic 50`, will process an image as a mosaic with tiles 50 wide and 50 high'
        return
    
    image_data, image_width, image_height = handle_file.load_file(original_file_name)

    if square_width < 1:
        print 'Must enter a square width of 1 or more'
        return
    elif square_width > image_width: 
        print 'Must enter a square width less than the image width'
        return
    elif square_width > image_height:
        print 'Must enter a square width less than the image height'
        return

    if process_name == 'mosaic':
        new_image_data = mosaic.process_image_data(image_data, image_width, image_height, square_width)
    else:
        print '%s is not an option. Please use one of - mosaic | add more' %(process_name)
        return

    handle_file.save_new_file(original_file_name, process_name, square_width, new_image_data)

run_application()