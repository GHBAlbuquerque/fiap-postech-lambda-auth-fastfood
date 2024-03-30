terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>3.27"
    }
  }

#  required_version = ">=0.14.9"

  backend "s3" {
    bucket = "terraform-state-backend-postech"
    key    = "arn:aws:s3:::terraform-state-backend-postech"
    region = "east-us-1"
  }
}


provider "aws" {
  region  = "east-us-1"
}

