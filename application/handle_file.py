from PIL import Image

def rm_folders_from_path(original_file_path):
    return original_file_path.split('/')[-1]

def load_file(file_location):
    image_file = Image.open(file_location)
    image_width, image_height = image_file.size
    image_data = image_file.load() 
    return image_data, image_width, image_height

def save_new_file(original_file_path, process_name, square_width, new_image_data):
    original_file_name = rm_folders_from_path(original_file_path)
    new_file_name = 'images/%s_%s_%s' %(process_name, square_width, original_file_name)
    new_image_data.save(new_file_name)
