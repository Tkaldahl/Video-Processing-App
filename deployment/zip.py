import os
import zipfile

def create_zip_with_ignore(source_folder, output_zip, ignore_files, ignore_dirs):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_folder):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            for file in files:
                if file not in ignore_files:
                    zipf.write(os.path.join(root, file))
# Usage
source_folder = '.'
output_zip = 'deployment/Video_Processing_App.zip'
ignore_files = []
ignore_dirs = ['.git', 'venv', 'deployment']
create_zip_with_ignore(source_folder, output_zip, ignore_files, ignore_dirs)