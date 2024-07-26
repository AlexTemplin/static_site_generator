import os 
import shutil

def copy_files_recursive(source, destination):
    # Clear the destination directory
    if os.path.exists(destination):
        print(f"Removing existing directory: {destination}")
        shutil.rmtree(destination)

    print(f"Creating destination directory: {destination}")
    os.mkdir(destination)

    # List the contents of the source directory
    for item in os.listdir(source):
        print(f"Processing item: {item}")
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)

        # Check if the item is a file or directory
        if os.path.isfile(source_item):
            print(f"Copying file: {source_item} to {destination_item}")
            shutil.copy(source_item, destination_item)
        elif os.path.isdir(source_item):
            print(f"Entering directory: {source_item}")
            copy_files_recursive(source_item, destination_item) # Recursive call