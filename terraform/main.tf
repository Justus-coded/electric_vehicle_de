terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.24.0"
    }
  }
}


provider "google" {
  credentials = var.credentials #not necesssary if credentials is saved in system using  export GOOGLE_CREDENTIALS
  project     = var.project
  region      = "us-central1"
}

resource "google_storage_bucket" "electric-vehicle-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = false

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "electric_vehicle_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}

