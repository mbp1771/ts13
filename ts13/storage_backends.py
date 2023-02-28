from storages.backends.azure_storage import AzureStorage
from azure.identity import DefaultAzureCredential

class MediaStorage(AzureStorage):
    token_credential = DefaultAzureCredential()
    location = 'media'
    overwrite_files = False