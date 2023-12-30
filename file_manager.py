# file_manager.py

import os
import shutil
import stat
import time

def create_file(file_path):
    with open(file_path, "w"):
        pass

def delete_file(file_path):
    os.remove(file_path)

def rename_file(old_path, new_path):
    os.rename(old_path, new_path)

def create_directory(directory_path):
    os.makedirs(directory_path)

def delete_directory(directory_path):
    shutil.rmtree(directory_path)

def copy_file(source_path, destination_path):
    shutil.copy2(source_path, destination_path)

def move_file(source_path, destination_path):
    shutil.move(source_path, destination_path)

def list_files(directory_path="."):
    return os.listdir(directory_path)

def get_file_info(file_path):
    file_stat = os.stat(file_path)
    size = file_stat.st_size
    permissions = stat.filemode(file_stat.st_mode)
    creation_time = time.ctime(file_stat.st_ctime)

    return {
        "size": size,
        "permissions": permissions,
        "creation_time": creation_time
    }

def search_files(directory_path, query):
    matching_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if query.lower() in file.lower():
                matching_files.append(os.path.join(root, file))
    return matching_files
