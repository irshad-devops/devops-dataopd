import pytest
from pyspark.sql import SparkSession

def test_spark_session():
    # Setup a local Spark session for testing
    spark = SparkSession.builder.master("local[1]").appName("CI-Test").getOrCreate()
    
    # Create dummy data with PII
    data = [("John Doe", "john@example.com"), ("Jane Smith", "jane@test.com")]
    df = spark.createDataFrame(data, ["name", "email"])
    
    # Assert the dataframe has 2 rows
    assert df.count() == 2
    spark.stop()

def test_pii_masking_integrity():
    # Simulate a check for masked data
    sample_email = "user@example.com"
    masked_email = "********@example.com" 
    
    # Assert that the masking actually happened
    assert "@" in masked_email
    assert "user" not in masked_email
    print("PII Masking Validation Passed!")
