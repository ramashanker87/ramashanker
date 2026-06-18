terraform {
  backend "s3" {
    bucket         = "rama-day12-tf-state-20260602"
    key            = "day12/dev/terraform.tfstate"
    region         = "us-east-1"
    profile         = "devops"
    dynamodb_table = "rama-day12-terraform-locks"
    encrypt        = true
  }
}