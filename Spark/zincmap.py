# Import Modules
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType
import pyspark.sql.functions as F
from db_config import url, properties
from mhfp.encoder import MHFPEncoder
from pyspark.sql.types import IntegerType, StringType
sudo apt-get install libboost-all-dev
mhfp_encoder = MHFPEncoder()
spark = SparkSession.builder.getOrCreate()

# Defined multiple UDF via PySpark Sql appfunctions.py module
def filename(path):
    return path
countCarbons = F.udf(lambda x : str(x).lower().count('c'), IntegerType())
sourceFile = F.udf(filename, StringType())
mhfp_smiles = F.udf(lambda x : mhfp_encoder.encode(x, radius=3, rings=True, kekulize=True, sanitize=True), StringType())
# Created DataFrames here with the new columns that I required and dropped the duplicates
df = spark.read.format('csv').option('delimiter','\t').option('header', 'false')\
    .load('s3a://zincdata/zinc/AA/AAAA.txt')
df = df.withColumn('mhfp', mhfp_smiles('smiles'))
df = df.dropDuplicates(['smiles'])
df.show()
# Performed my dataframe write with the help of jdbc
#df.write.jdbc(url='jdbc:%s' % url, table="zincmap", mode='append', properties=properties)










