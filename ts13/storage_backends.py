from storages.backends.azure_storage import AzureStorage
from azure.identity import DefaultAzureCredential

class MediaStorage(AzureStorage):
    account_name = 'musicts13'
    azure_container = 'ts13'
    token_credential = DefaultAzureCredential()
    location = 'media'
    overwrite_files = False