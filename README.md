# End-to-End-ML-Project-with-MLflow

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update schema.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py 
9. Update the dvc.yaml

# How to run?
## STEPS:
Clone the repository

https://github.com/stordd13/End-to-end-ML-Project-with-MLflow

### STEP 01 - Create a conda environment after opening the repository

conda create -n mlproj python=3.9 -y
conda activate mlproj

### STEP 02 - install the requirements
pip install -r requirements.txt

# Finally run the following command
python app.py
Now,

open up you local host and port
MLflow
Documentation

cmd
mlflow ui
dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/stordeur.bru/End-to-End-ML-Project-with-MLflow.mlflow 
MLFLOW_TRACKING_USERNAME=stordeur.bru 
MLFLOW_TRACKING_PASSWORD=fcd028c788a5f8d79dce5bfe08d8d2145df543df 
python script.py


Run this to export as env variables:

export MLFLOW_TRACKING_URI=https://dagshub.com/stordeur.bru/End-to-End-ML-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=stordeur.bru 

export MLFLOW_TRACKING_PASSWORD=fcd028c788a5f8d79dce5bfe08d8d2145df543df 


# AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


## Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

## Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 648772456581.dkr.ecr.eu-west-3.amazonaws.com/
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = eu-west-3

AWS_ECR_LOGIN_URI = 648772456581.dkr.ecr.eu-west-3.amazonaws.com/

ECR_REPOSITORY_NAME = mlproj

# About MLflow
MLflow

Its Production Grade
Trace all of your expriements
Logging & tagging your model