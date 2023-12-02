import os
import zipfile
from video_service.s3_service import upload_file_obj_to_s3
import os

def create_zip_with_ignore(source_dir, output_zip, ignore_files, ignore_dirs):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            for file in files:
                if file not in ignore_files:
                    zipf.write(os.path.join(root, file))



def delete_dirs_by_name(source_dir, dir_names):
    for root, dirs, files in os.walk(source_dir):
        for dir in dirs:
            if dir in dir_names:
                dir_path = os.path.join(root, dir)
                os.rmdir(dir_path)


# Zip the dependencies
# dependencies_source_folder = 'aws_lambda_env/lib/python3.9/site-packages'
# dependencies_output_zip = 'my_deployment_package.zip'
# dependencies_ignore_files = []
# dependencies_ignore_dirs = ['urllib3', 'six', 'jmespath', 'python-dateutil', 'botocore', 's3transfer', 'boto3']
# create_zip_with_ignore(dependencies_source_folder, dependencies_output_zip, dependencies_ignore_files, dependencies_ignore_dirs)

# Zip the source code
source_code_source_folder = '.'
source_code_output_zip = 'Video_Processing_App.zip'
source_code_ignore_files = []
source_code_ignore_dirs = ['.git', '.gitignore', 'venv', 'deployment', 'aws_lambda_env', "Processed_Videos", "test_resources"]
create_zip_with_ignore(source_code_source_folder, source_code_output_zip, source_code_ignore_files, source_code_ignore_dirs)

# Upload the zip files to S3
upload_file_obj_to_s3(source_code_output_zip, 'power60', 'deployment-versions/Video_Processing_App.zip')

# # Delete the zip files
# dirs_to_delete = [dependencies_output_zip, source_code_output_zip]
# delete_dirs_by_name('.', dirs_to_delete)