variable "project" {
  description = "Project"
  default     = "electricvehicles-420015"
}

variable "credentials" {
  description = "Credentials"
  default     = "/workspaces/electric_vehicle_de/keys.json"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}



variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My Bigquery Dataset Name"
  default     = "electric_vehicles"
}


variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "electricvehicles-420015-bucket"
}


variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}