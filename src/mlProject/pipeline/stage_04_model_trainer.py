from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from pathlib import Path


STAGE_NAME = "Model Trainer stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):  
        config = ConfigurationManager()
        trainer_config = config.get_model_trainer_config()
        trainer = ModelTrainer(config=trainer_config)
        trainer.train()
    
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x============x")
    except Exception as e:
        logger.exception(e)
        raise(e)
