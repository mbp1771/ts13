from storages.backends.azure_storage import AzureStorage
from msrestazure.azure_active_directory import MSIAuthentication

class MediaStorage(AzureStorage):
    account_name = 'musicts13'
    azure_container = 'ts13'
    token_credential = MSIAuthentication()
    location = 'media'
    overwrite_files = False