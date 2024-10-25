<h1 align="center">Chicken Disease Classification MLOps Project 🐔</h1>

<p align="center">
  <img src="https://github.com/JSaez97/JSaez97/blob/assets/chicken_disease_banner.png" alt="Javier_Saez_Banner">
</p>

<h2 align="left">Overview</h2>

The Chicken Disease Classification MLOps Project is an end-to-end solution that uses Convolutional Neural Networks (CNNs) to detect and classify chicken diseases like the Coccidiosis, NCD or Salmonella from images, it also can detect if the chicken is healthy. It integrates a complete MLOps pipeline with Docker for containerization, AWS for cloud deployment, and GitHub Actions for CI/CD, ensuring automated, scalable, and efficient model deployment with minimal manual intervention. This project could help farmers and veterinarians monitor poultry health in real time.

<h2 align="left">Key Objectives</h2>

▶️  &nbsp;Disease Detection and Classification: Accurately identify different chicken diseases from images using CNN models.

▶️  &nbsp;Automation: Automate the process of data ingestion, model training, and deployment through MLOps principles.

▶️  &nbsp;Cloud Scalability: Deploy the app in a cloud environment (AWS ECS) for easy access, scalability, and reliability.

<h2 align="left">Datasets</h2>

The chosen dataset for this project is the [Chicken Disease Image Classification](https://www.kaggle.com/datasets/allandclive/chicken-disease-1).

<h2 align="left">Future Improvements</h2>

▶️  &nbsp; Create a custom web site related to the topic.

<h2 align="left">Project Setup</h2>

Clone the project from the repository
```
git clone https://github.com/JSaez97/Chicken_Disease_Classification_MLOps_Project.git
```
Change working directory to the project repository
```
cd "D:/example/chicken-disease-mlops"
```
Create conda environment
```
conda create -n chickenenv python=3.8 -y # Change environment name (in this case "chickenenv") according to your preferences
```
```
conda activate chickenenv
```
Install project dependencies
```
pip install -r requirements.txt
```
Execute the following command
```
python app.py
```
To test the script locally
```
Copy one of the addresses and paste it in your web browser, for example: http://x.x.x.x:80
```
<h2 align="left">CICD Deployment on AWS</h2>
<h3 align="left">Getting Started with AWS Setup</h3>

1. **Login to AWS Console**:
   - Access your AWS account to configure the necessary services and permissions for deployment.

2. **Create an IAM User for Deployment**:
   - Configure the user with the following permissions to access required AWS services:
     - **EC2 Access**: For managing the virtual machine.
     - **ECR Access**: For storing Docker images in AWS's Elastic Container Registry.

3. **Set Up Permissions and Policies**:
   - Attach the following policies to the IAM user to allow access:
     - **AmazonEC2ContainerRegistryFullAccess**: Grants full access to ECR.
     - **AmazonEC2FullAccess**: Grants full control over EC2 resources.

### Deployment Steps

1. **Create an ECR Repository**:
   - In AWS ECR, create a repository to store and version your Docker images.
   - Save the repository URI for later use (e.g., `566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken`).

2. **Build Docker Image of the Source Code**:
   - Package the application code into a Docker image to prepare it for deployment.

3. **Push Docker Image to ECR**:
   - Push the built Docker image to your ECR repository to make it accessible for EC2.

4. **Launch EC2 Instance**:
   - Create an EC2 instance (e.g., Ubuntu) to host the application.

5. **Install Docker on EC2**:
   - SSH into the EC2 instance and run the following commands to install Docker:
     ```bash
     # Optional updates
     sudo apt-get update -y
     sudo apt-get upgrade

     # Install Docker
     curl -fsSL https://get.docker.com -o get-docker.sh
     sudo sh get-docker.sh

     # Grant Docker permissions to the user
     sudo usermod -aG docker ubuntu
     newgrp docker
     ```

6. **Pull Docker Image from ECR on EC2**:
   - Use Docker commands on the EC2 instance to pull the image from ECR.

7. **Run Docker Image on EC2**:
   - Launch the Docker container on the EC2 instance to start your application.

### Configuring GitHub Actions for CI/CD

1. **Configure EC2 as a Self-Hosted Runner**:
   - Go to your GitHub repository settings and navigate to `Actions > Runners > New self-hosted runner`.
   - Follow the provided instructions to set up your EC2 instance as a self-hosted runner for GitHub Actions.

2. **Setup GitHub Secrets**:
   - In your GitHub repository, add the following secrets under `Settings > Secrets`:
     - `AWS_ACCESS_KEY_ID`
     - `AWS_SECRET_ACCESS_KEY`
     - `AWS_REGION` (e.g., `us-east-1`)
     - `AWS_ECR_LOGIN_URI` (e.g., `566373416292.dkr.ecr.us-east-1.amazonaws.com`)
     - `ECR_REPOSITORY_NAME` (e.g., `chicken`)

