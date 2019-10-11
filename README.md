# Smiles to Drug Discovery
## Pipeline
### Overview
Allows for chemical structure virtual screening for purchasability
### Current Step
Ingestion via PySpark of data from zinc database
Uncompress via PySpark and then onto S3
PySpark retreive extracted files as RDD 
Mapped RDD to DataFrames then onto PostgreSQL
Data displayed via Flask App 
