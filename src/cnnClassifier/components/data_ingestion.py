import os
import urllib.request as request
import zipfile
import shutil
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"{self.config.local_data_file} already exists and the size is {get_size}.")
    
    
    def extract_zip_file(self):
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        # Use shutil to extract the file
        try:
            shutil.unpack_archive(self.config.local_data_file, unzip_path)
            logger.info(f"Extracted {self.config.local_data_file} to {unzip_path}")
        except shutil.ReadError:
            logger.error(f"Failed to extract {self.config.local_data_file}. It might not be a valid archive.")