variable "bucket_name" {
  description = "The name of the S3 bucket for flight data"
  type        = string
  default     = "marwat-flight-data-2026" # Change this if it's taken
}

variable "db_username" {
  description = "Database administrator username"
  type        = string
  default     = "dbadmin"
}

variable "db_password" {
  description = "Database administrator password"
  type        = string
  sensitive   = true # This hides the password in the terminal logs
}
