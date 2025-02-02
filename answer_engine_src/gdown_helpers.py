import gdown
import os 
def create_folder_if_not_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def get_gdrive_file(url, output):
    root_folder = os.path.dirname(output)
    create_folder_if_not_exists(root_folder)
    gdown.download(url, output, quiet=False)
    print(f"Downloaded file saved as {output}")
    