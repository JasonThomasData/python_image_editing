from PIL import Image

def load_file(original_file_name):
    file_location = 'images/%s' %(original_file_name)
    image_file = Image.open(file_location)
    image_width, image_height = image_file.size
    image_data = image_file.load() 
    return image_data, image_width, image_height

def save_new_file(original_file_name, process_name, square_width, new_image_data):
    new_file_name = 'images/%s_%s_%s' %(process_name, square_width, original_file_name)
    new_image_data.save(new_file_name)