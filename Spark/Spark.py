import boto3
import pyspark
from pyspark.sql import SparkSession

s3 = boto3.resource('s3')

s3.Bucket('zincdata').download_file('tranches/AA/AAHL/AAAAHL.xaa.db2', 'file.db2')

spark = SparkSession.builder.getOrCreate()

df = spark.read.option('header','true').format('csv').option('delimiter', '\t').load('file.db2')

df.show()