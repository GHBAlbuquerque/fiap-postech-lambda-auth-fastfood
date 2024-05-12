variable "project_name" {
  default = "postech-lambda-auth-fastfood"
}

variable "region" {
  default = "us-east-1"
}

variable "profile" {
  default = "default"
}

variable "lab_role_arn" {
  default = "arn:aws:iam::067184771399:role/LabRole"
}

variable "tf_state_bucket_key" {
  default = "terraform-state-backend-postech-new"
}
