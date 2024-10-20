from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed successfully.")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e