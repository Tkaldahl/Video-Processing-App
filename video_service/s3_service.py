import boto3

s3_client = boto3.client('s3')

def upload_file_obj_to_s3(file_path, bucket, file_name):
    with open(file_path, 'rb') as file_obj:
        s3_client.upload_fileobj(file_obj, bucket, file_name)


# Tests

def _test_file_obj_upload():
    upload_file_obj_to_s3('test_resources/hello_world.txt', 'power-60', 'testing/hello-world-test-2.txt')

_test_file_obj_upload()
