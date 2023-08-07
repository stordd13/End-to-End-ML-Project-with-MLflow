from mlProject.entity.config_entity import DataTransformationConfig
import os 
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from pathlib import Path


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config

## Note : I can add a lot of function like scaler, OHE , PCA but the purpose 
# #of the project is to design the pipelines so I will only do train test split for now
    def train_test_splitting(self):

        data = pd.read_csv(Path(self.config.data_path))

        train, test=  train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"), index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)
    