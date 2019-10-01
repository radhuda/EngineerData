import pyspark
from pyspark.sql import SparkSession
sc = pyspark.SparkContext()
spark = SparkSession.builder.getOrCreate()

url = 'postgresql://10.0.0.11:5432/zincdatabase'
properties = {'user': 'postgres', 'password': 'rad1234', 'driver': "org.postgresql.Driver"}


df = spark.read.format('csv').option('delimiter','\t').option('header', 'true').load('s3a://zincdata/zinc/*/*.txt')
df.write.jdbc(url='jdbc:%s' % url, table="zinc_full_table", mode='append', properties=properties)










