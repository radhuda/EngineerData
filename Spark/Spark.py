import pyspark
import pcapkit
sc = pyspark.SparkContext(appName='try')



output =  pcapkit.extract(fin=PCAP_File, nofile = True)

print(output)
