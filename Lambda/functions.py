import urllib
import boto3
s3 = boto3.client('s3')
listlink = 'http://files.docking.org/catalogs/40/'
def downloadl(x):
    if len(str(x)[3:-3]) > 1:
        local_filename, headers = urllib.request.urlretrieve(
            listlink + str(x)[3:-3] + '/' + 'sdi-mol2-leads')
        f = open(local_filename, 'rb')
        for lines in f:
            file_url = str(lines)[2:-3]
            file, headers = urllib.request.urlretrieve(file_url)
            key = 'leads' + '/' + str(lines)[27:-3]
            bucket = 'zincdata'
            s3.upload_fileobj(open(file, 'rb'), Bucket=bucket, Key=key)
            file_url2 = str(lines)[2:-18] + '.prot.txt'
            txt, headers2 = urllib.request.urlretrieve(file_url2)
            key2 = 'leads' + '/' + str(lines)[27:-18] + '.txt'
            s3.upload_fileobj(open(txt, 'rb'), Bucket=bucket, Key=key2)
        local_filenamefrag, headers = urllib.request.urlretrieve(
            listlink + str(x)[3:-3] + '/' + 'sdi-mol2-frags')
        t = open(local_filenamefrag, 'rb')

        for lines in t:
            file_url = str(lines)[2:-3]
            file, headers = urllib.request.urlretrieve(file_url)
            key = 'frags' + '/' + str(lines)[27:-3]
            bucket = 'zincdata'
            s3.upload_fileobj(open(file, 'rb'), Bucket=bucket, Key=key)
            file_url2 = str(lines)[2:-18] + '.prot.txt'
            txt, headers2 = urllib.request.urlretrieve(file_url2)
            key2 = 'frags' + '/' + str(lines)[27:-18] + '.txt'
            s3.upload_fileobj(open(txt, 'rb'), Bucket=bucket, Key=key2)
    else:
        None