from stringFunctions import remove_white_spaces
import pyspark
from pyspark.sql import SparkSession
sc = pyspark.SparkContext()
spark = SparkSession.builder.getOrCreate()

url = 'postgresql://10.0.0.11:5432/zincdatabase'
properties = {'user': 'postgres', 'password': 'rad1234', 'driver': "org.postgresql.Driver"}

rdd = sc.textFile('s3a://zincdata/key2Files.txt').collect()
df = spark.read.format('csv').option('delimiter','\t')\
    .load('s3a://zincdata/frags/catalogs/30/molportbb/tranches/AA/xaaa.txt').toDF("smiles",
         "zinc_id","files.db2", "inchikey", "net_charge", "mwt", "tranches2", "logp",'substance_unk',
         "reactive_cat", "substane_sect", "tranche_name", "substance_struct", "substance_feature")
for x in rdd:
    try:
        newdf = spark.read.format('csv').option('delimiter','\t').load('s3a://zincdata/' + x).toDF("smiles",
         "zinc_id","files.db2", "inchikey", "net_charge", "mwt", "tranches2", "logp",'substance_unk',
         "reactive_cat", "substane_sect", "tranche_name", "substance_struct", "substance_feature")

        df = df.union(newdf)
    except:
        print(x)
df.write.parquet('s3a://zincdata/parquet3/')








