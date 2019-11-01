import pyspark
import urllib
import boto3
import gzip
from smart_open import open
s3 = boto3.client('s3')
listlink = 'http://files.docking.org/catalogs/40/'
sc = pyspark.SparkContext(appName='getFile')

def downloadToS3(x):
    bucket = 'zincdata/'
    if len(str(x)[3:-3]) > 1:
        local_filename, headers = urllib.request.urlretrieve(
            listlink + str(x)[3:-3] + '/' + 'sdi-mol2-leads')
        for lines in open(local_filename, 'rb'):
            file_url = str(lines)[2:-3]
            file, headers = urllib.request.urlretrieve(file_url)
            key = 'leads' + '/' + str(lines)[27:-3]
            with open('s3://' + bucket + key,'wb') as leadout:
                for line in gzip.open(file,'rb'):
                    leadout.write(line)
            file_url2 = str(lines)[2:-18] + '.prot.txt'
            txt, headers2 = urllib.request.urlretrieve(file_url2)
            key2 = ('leads' + '/' + str(lines)[27:-18] + '.txt')
            with open('s3://' + bucket + key2, 'w') as leadtxtout:
                for line in open(txt,'r'):
                    leadtxtout.write(line)

        local_filenamefrag, headers = urllib.request.urlretrieve(
            listlink + str(x)[3:-3]+ '/' + 'sdi-mol2-frags')
        for lines in open(local_filenamefrag, 'rb'):
            file_url = str(lines)[2:-3]
            file, headers = urllib.request.urlretrieve(file_url)
            key = 'frags' + '/' + str(lines)[27:-3]
            with open('s3://' + bucket + key, 'wb') as fragout:
                for line in gzip.open(file,'rb'):
                    fragout.write(line)
            file_url2 = (str(lines)[2:-18] + '.prot.txt')
            txt, headers2 = urllib.request.urlretrieve(file_url2)
            key2 = 'frags' + '/' + str(lines)[27:-18] + '.txt'
            with open('s3://' + bucket + key2, 'w') as fragtxtout:
                for line in open(txt,'r'):
                    fragtxtout.write(line)

listofkeys = open('http://files.docking.org/catalogs/40/list.save', 'rb')

list50 = ['alfa','aronisbb','bachem','cdivbbe-v','cdivbbe', 'cdive','chbrbbe','chbre','combiblocksbb',
          'enamine', 'enaminebb', 'frinton', 'frontier', 'frontierbb', 'keyo', 'keyobb', 'keyobio', 'matrix',
          'mayb', 'maybbb', 'mce', 'molportbbe', 'molporte', 'ryan', 'ryanbb', 'selleck', 'sial', 'sialbb', 'specs',
          'tocris', 'trc', 'vitasm', 'vitasmbb'
          ]


rdd = sc.parallelize(listofkeys)
rdd.foreach(lambda x : downloadToS3(x))

