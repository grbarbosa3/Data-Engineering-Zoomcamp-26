terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.25.0"
    }
  }
}

provider "google" {
  project = "zoomcamp-491517"
  region  = "southamerica-east1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "terra-bucket-793003"
  location      = "southamerica-east1"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}