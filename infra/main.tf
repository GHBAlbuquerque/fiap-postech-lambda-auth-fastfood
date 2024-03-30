provider "aws" {
  version = "~> 5.0"
  region  = "us-east-1"
}
#  required_version = ">=0.14.9"

terraform {
  backend "s3" {
    bucket = "terraform-state-backend-postech"
    key    = "arn:aws:s3:::terraform-state-backend-postech"
    region = "east-us-1"
  }
}


