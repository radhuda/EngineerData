# Spark Directory

## Getting to know the PySpark Work
 
This is the directory that the source file for PySpark resides. In here I have the python
file named `Spark.py`

There are multiple parts to the code.

1. I defined  Defined multiple UDF via PySpark Sql functions module
```
countCarbons = F.udf(lambda x : str(x).lower().count('c'), IntegerType())
countNitrogens = F.udf(lambda x : str(x).lower().count('n'), IntegerType())
countOxygens = F.udf(lambda x : str(x).lower().count('o'), IntegerType())
```
2. I Created DataFrames here with the new columns that I required and dropped the duplicates

```
df = spark.read.format('csv').option('delimiter','\t').option('header', 'true')\
    .load('s3a://zincdata/zinc/*/*.txt')
df = df.withColumn('Carbons', countCarbons('smiles'))
df = df.withColumn('Nitrogens', countNitrogens('smiles'))
df = df.withColumn('Oxygens', countOxygens('smiles'))
df = df.dropDuplicates(['smiles'])
```
3. Lastly performed my dataframe write with the help of jdbc```

```
df.write.jdbc(url='jdbc:%s' % url, table="zinc_table", mode='append', properties=properties)

```
