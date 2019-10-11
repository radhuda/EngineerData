# Import Modules
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType
import pyspark.sql.functions as F
from db_config import url, properties

spark = SparkSession.builder.getOrCreate()


# Defined multiple UDF via PySpark Sql appfunctions.py module
def filename(path):
    return path
countCarbons = F.udf(lambda x : str(x).lower().count('c'), IntegerType())
countNitrogens = F.udf(lambda x : str(x).lower().count('n'), IntegerType())
countOxygens = F.udf(lambda x : str(x).lower().count('o'), IntegerType())
sourceFile = F.udf(filename, StringType())

# Created DataFrames here with the new columns that I required and dropped the duplicates
df = spark.read.format('csv').option('delimiter','\t').option('header', 'true')\
    .load('s3a://zincdata/zinc/*/*.txt')
df = df.withColumn('carbons', countCarbons('smiles'))
df = df.withColumn('nitrogens', countNitrogens('smiles'))
df = df.withColumn('oxygens', countOxygens('smiles'))
df = df.withColumn('filename', sourceFile(F.input_file_name()))
df = df.dropDuplicates(['smiles'])

# Performed my dataframe write with the help of jdbc
df.write.jdbc(url='jdbc:%s' % url, table="zinc", mode='append', properties=properties)










