# Electric Vehicle Data Engineering Project

## Overview
This project aims to explore and gain insights into the use of electric vehicles (EVs) in the United States. The dataset utilized for this project was obtained from [Data.gov](https://catalog.data.gov/dataset/electric-vehicle-population-data).

## Project Workflow

### Cloud Infrastructure Setup
1. **GCP Infrastructure Creation**
   - Create a project in Google Cloud Platform (GCP).
   - Create a service account with the following roles: Storage Admin, BigQuery Admin, and Compute Admin.
   - Generate service account keys and download the key (.json file).

2. **Terraform Setup**
   - Install Terraform:
     ```bash
     wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
     echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
     sudo apt update && sudo apt install terraform
     ```
   - Create a new folder (e.g., `terraform`) and navigate into it.
   - Create `main.tf` and `variables.tf` files.
   - Update `main.tf` with project ID, credentials, region, and location using the variables declared in `variables.tf`.
   - Update `main.tf` with Google Cloud Storage bucket name and BigQuery dataset name.
   - Set service account key as an environment variable:
     ```bash
     export GOOGLE_CREDENTIALS='/path/to/your/keys.json'
     ```
   - Initialize Terraform and apply changes:
     ```bash
     terraform init
     terraform plan
     terraform apply
     ```

### Data Orchestration
1. **Mage and Docker Setup**
   - Create a folder for Mage (e.g., `Mage`).
   - Add a Dockerfile to the folder that contains the Mage image:
     ```Dockerfile
     FROM mageai/mageai:latest
     
     ARG USER_CODE_PATH=/home/src/${PROJECT_NAME}
     
     COPY requirements.txt ${USER_CODE_PATH}requirements.txt 
     
     RUN pip3 install -r ${USER_CODE_PATH}requirements.txt
     ```
   - Add a `docker-compose.yml` file to include the project name, Dockerfile, GCP service keys, and other environment variables.

2. **Running Mage**
   - Build and spin up Mage on localhost:
     ```bash
     docker-compose up
     ```
   - This may take some time to initialize.

3. **Pipeline Creation**
   - In Mage, create a pipeline to load the data into Google Cloud Storage and BigQuery.

### Data Transformation

#### dbt Cloud Setup
1. **Create a New Project in dbt**
   - Sign in to dbt Cloud and create a new project.
   - Add a project name and select BigQuery as the data source.
   - Include the service account keys for authentication.
   - Set up a repository to run your transformations and create the project.

2. **Initialize dbt Project**
   - Click 'initialize dbt project' and then 'commit and sync'.

3. **Model Creation and Transformation**
   - Create your SQL files in the models directory for transformation.
   - Perform data transformation using dbt:
     ```bash
     dbt run
     ```

4. **Resources**
   - [dbt Documentation for BigQuery](https://docs.getdbt.com/guides/bigquery?step=8)

### Dashboard Creation

1. **Access Looker Studio**
   - Go to [Looker Studio](https://lookerstudio.google.com).

2. **Create a New Report**
   - Create a new report in Looker Studio.
   - Connect to BigQuery as the data source.
   - Select datasets to use for building the dashboard.

3. **Dashboard Design**
   - Design your dashboard in Looker Studio.
   - Include relevant visualizations and insights.

4. **Dashboard Image**
   ![Electric Vehicle Dashboard](https://lookerstudio.google.com/embed/reporting/fb76d5d5-193d-46b9-8b06-b75b885f9b03/page/RpiwD)



## Resources
- [Google Cloud Platform](https://cloud.google.com/)
- [Terraform Documentation](https://learn.hashicorp.com/terraform)
- [Mage Documentation](https://docs.mage.ml/)
- [Docker Documentation](https://docs.docker.com/)
- [dbt Documentation](https://docs.getdbt.com/)
- [Looker Documentation](https://docs.looker.com/)
- [Data.gov](https://www.data.gov/) - Source of the Electric Vehicle Population Data


