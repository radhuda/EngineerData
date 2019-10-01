import boto3

s3 = boto3.client('s3')
import pyspark

sc = pyspark.SparkContext()


rdd= sc.textFile('rad1.txt').collect()

for key in rdd :
    s3.delete_object(Bucket='zincdata', Key=key)

