import os
import zipfile
from video_service.s3_service import upload_file_obj_to_s3

def create_zip_with_ignore(source_folder, output_zip, ignore_files, ignore_dirs):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_folder):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            for file in files:
                if file not in ignore_files:
                    zipf.write(os.path.join(root, file))
# Usage
dependencies_source_folder = 'aws_lambda_env/lib/python3.9/site-packages'
dependencies_output_zip = 'Dependencies.zip'
dependencies_ignore_files = []
dependencies_ignore_dirs = ['urllib3', 'six', 'jmespath', 'python-dateutil', 'botocore', 's3transfer', 'boto3']
create_zip_with_ignore(dependencies_source_folder, dependencies_output_zip, dependencies_ignore_files, dependencies_ignore_dirs)


source_folder = '.'
output_zip = 'deployment/Video_Processing_App.zip'
ignore_files = []
ignore_dirs = ['.git', 'venv', 'deployment', 'aws_lambda_env']

create_zip_with_ignore(source_folder, output_zip, ignore_files, ignore_dirs)
upload_file_obj_to_s3('deployment/Video_Processing_App.zip', 'power-60', 'lambdaDeployments/Video_Processing_App.zip')