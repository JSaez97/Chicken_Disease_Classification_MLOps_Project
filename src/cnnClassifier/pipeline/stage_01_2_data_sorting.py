import os
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_sorting import DataSorting
from cnnClassifier import logger


# Definir el nombre de la etapa para logging
STAGE_NAME = "Data Sorting and Transfer"

class DataSortingAndTransferPipeline:
    def __init__(self):
        pass

    def main(self):
        # Cargar la configuración desde ConfigurationManager
        config = ConfigurationManager()

        # Obtener la configuración para data sorting
        data_sorting_config = config.get_data_sorting_config()

        # Ejecutar la etapa de data sorting
        data_sorting = DataSorting()
        data_sorting.sort_images(config=data_sorting_config)  # Método para ordenar las imágenes

        # Ejecutar la etapa de transferencia y limpieza de carpetas
        data_sorting.transfer_and_clean_folders(data_sorting_config)  # Método para la transferencia y limpieza

if __name__ == '__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} started")
        obj = DataSortingAndTransferPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e