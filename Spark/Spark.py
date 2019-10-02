# Import Modules
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
import pyspark.sql.functions as F
from db_config import url, properties

spark = SparkSession.builder.getOrCreate()

# Defined multiple UDF via PySpark Sql functions module
countCarbons = F.udf(lambda x : str(x).lower().count('c'), IntegerType())
countNitrogens = F.udf(lambda x : str(x).lower().count('n'), IntegerType())
countOxygens = F.udf(lambda x : str(x).lower().count('o'), IntegerType())

# Created DataFrames here with the new columns that I required and dropped the duplicates
df = spark.read.format('csv').option('delimiter','\t').option('header', 'true')\
    .load('s3a://zincdata/zinc/*/*.txt')
df = df.withColumn('Carbons', countCarbons('smiles'))
df = df.withColumn('Nitrogens', countNitrogens('smiles'))
df = df.withColumn('Oxygens', countOxygens('smiles'))
df = df.dropDuplicates(['smiles'])

# Performed my dataframe write with the help of jdbc
df.write.jdbc(url='jdbc:%s' % url, table="zinc_table", mode='append', properties=properties)










