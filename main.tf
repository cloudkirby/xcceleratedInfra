terraform {
  backend "gcs" {
    bucket = "anthony-infra-bucket"
    prefix = "terraform/state"
  }
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.8.0"
    }
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "7.7.0"
    }
  }
}

provider "google" {
  project = var.project
  region  = var.region
  zone    = var.zone
}

variable "image_tag" {
  type = string
  description = "The SHORT_SHA from cloudbuild"
}

resource "google_cloud_run_v2_service" "default" {
  location = "europe-west4"
  name     = "anthony-app-service"
  deletion_protection = false

  template {
    containers {
      image = "europe-west4-docker.pkg.dev/anthony-infra-ci-project/anthony-infra-repo/anthony-infra:${var.image_tag}"
    }
  }
}
