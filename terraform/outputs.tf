output "s3_bucket_id" {
  value = aws_s3_bucket.data_lake.id
}

output "database_endpoint" {
  value = aws_db_instance.flight_db.endpoint
}

output "data_path_in_s3" {
  value = "s3://${aws_s3_bucket.data_lake.id}/raw/data.csv"
}
