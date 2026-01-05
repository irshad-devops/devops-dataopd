# Create the S3 Bucket (Data Lake)
resource "aws_s3_bucket" "data_lake" {
  bucket = var.bucket_name
  
  tags = {
    Name        = "FlightDataLake"
    Compliance  = "ISO27018"
    Environment = "Dev"
  }
}

# Compliance: Enable Server-Side Encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "lake_enc" {
  bucket = aws_s3_bucket.data_lake.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Data Ingestion: Upload your data.csv to the cloud
resource "aws_s3_object" "upload_csv" {
  bucket = aws_s3_bucket.data_lake.id
  key    = "raw/data.csv"
  source = "/home/marwat/Documents/Air-flow/dags/data.csv" # Adjusted path based on your folder structure
  etag   = filemd5("/home/marwat/Documents/Air-flow/dags/data.csv")
}

# Create RDS PostgreSQL Database
resource "aws_db_instance" "flight_db" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "15"
  instance_class       = "db.t3.micro"
  db_name              = "flight_analytics"
  username             = var.db_username
  password             = var.db_password
  parameter_group_name = "default.postgres15"
  skip_final_snapshot  = true
  publicly_accessible  = true
  storage_encrypted    = true # Key for ISO compliance
}
