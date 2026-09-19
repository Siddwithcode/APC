from abc import ABC, abstractmethod
class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self): pass
    @abstractmethod
    def download_file(self): pass
    @abstractmethod
    def delete_file(self): pass
class GoogleDrive(CloudStorage):
    def upload_file(self): print("Uploading to GDrive")
    def download_file(self): print("Downloading from GDrive")
    def delete_file(self): print("Deleting from GDrive")
GoogleDrive().upload_file()
