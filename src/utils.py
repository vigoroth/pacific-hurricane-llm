import os

def get_file_path(file_name, sub_dir):
    current_dir = os.path.dirname(os.path.abspath('__file__'))
    return os.path.join(current_dir, '..', sub_dir, file_name)