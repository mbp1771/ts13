"""from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False"""

from storages.backends.azure_storage import AzureStorage

class MediaStorage(AzureStorage):
    location = 'media'
    file_overwrite = False