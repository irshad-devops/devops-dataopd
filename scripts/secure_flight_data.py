from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sha2, concat, lit

# 1. Start Spark Session
spark = SparkSession.builder.appName("GDPR_Compliance_Masking").getOrCreate()

# 2. Load the validated data
df = spark.read.csv("/opt/airflow/dags/data.csv", header=True, inferSchema=True)

# 3. Security Task: Masking PII (Personally Identifiable Information)
# We will hash the country name to show how we can anonymize sensitive strings
# This satisfies GDPR 'Right to Anonymization'
secure_df = df.withColumn("masked_destination", sha2(col("DEST_COUNTRY_NAME"), 256))

# 4. Filter for GCC Region (Compliance with Regional Data Laws)
# We only want to save data for specific regions into a secure folder
gcc_countries = ["Saudi Arabia", "United Arab Emirates", "Qatar", "Kuwait", "Oman", "Bahrain"]
gcc_df = secure_df.filter(col("DEST_COUNTRY_NAME").isin(gcc_countries))

# 5. Save to "Secure Zone" (This would usually be an encrypted S3 bucket)
# For the demo, we save it locally in a 'secure' folder
gcc_df.write.mode("overwrite").parquet("/opt/airflow/dags/secure_output/")

print("Week 3 Task Complete: Data Masked and Filtered for Regional Compliance.")
spark.stop()
