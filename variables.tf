variable "environment" {
  description = "Env"
}

variable "name" {
  description = "Application Name"
  type        = string
}

locals {
  name_dash = "${var.name}-${var.environment}"
}

variable "region" {
  description = "AWS region for policies"
  type        = string
  default     = "us-east-1"
}

variable "lambda_name" {
  description = "Lambda Function Name"
  type        = string
}
