terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      Version = "~>3.27"
    }
  }

  required_version = ">=0.14.9"

   backend "s3" {
       bucket = "terraform-state-backend-postech"
       key    = "[Remote_State_S3_Bucket_Key]"
       region = "east-us-1"
   }
}
}

provider "aws" {
  version = "~>3.0"
  region  = "east-us-1"
}

