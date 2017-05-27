#!/usr/bin/python

import boto3
import sys, getopt

#Product Name to update
product = ''

#Template for Product
template = ''

#S3 bucket where template is uploaded and read from
s3bucket = ''

#Product ID
global productid

#S3 URL
s3url = ''

#version
version = ''

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hp:t:b:v:",["product=","template=","bucket=","version="])
   except getopt.GetoptError:
      print 'update_product.py -p <product> -t <template> -b <bucket> -v <version>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'update_product.py -p <product> -t <template> -b <bucket> -v <version>'
         sys.exit()
      elif opt in ("-p", "--product"):
         product = arg
      elif opt in ("-t", "--template"):
         template = arg
      elif opt in ("-b", "--bucket"):
         s3bucket = arg
      elif opt in ("-v", "--version"):
         version = arg

   # Call function_product_id to find the Product Id of the Product Name passed
   productid = find_product_id(product,productid='')
   check_product_version_exists(productid,version)
   update_s3_bucket(s3bucket,template)
   update_product(s3bucket,template,productid,version)


def find_product_id(product,productid):
  
  client = boto3.client('servicecatalog')
  response = client.search_products()
  for i in range(len(response['ProductViewSummaries'])):
    if response['ProductViewSummaries'][i]['Name'] == product:
      productid = response['ProductViewSummaries'][i]['ProductId']
      return productid
    else:
      print "product not present in the catalog"
      exit()

def check_product_version_exists(productid,version):

  client = boto3.client('servicecatalog')
  response = client.list_provisioning_artifacts(ProductId=productid)
  for i in range(len(response['ProvisioningArtifactDetails'])):
    if response['ProvisioningArtifactDetails'][i]['Name'] == version:
      print "productid with version already exists"
      exit()

def update_s3_bucket(s3bucket,template):
 
  file = './cfn-templates/'+template

  s3 = boto3.resource('s3')
  data = open(file, 'rb')
  s3.Bucket(s3bucket).put_object(Key=template, Body=data)
  
def update_product(s3bucket,template,productid,version):
  
  s3url = 'https://s3-ap-southeast-2.amazonaws.com/'+ s3bucket + '/' + template

  client = boto3.client('servicecatalog')
  response = client.create_provisioning_artifact(ProductId=productid,Parameters={'Name':version, 'Info': {'LoadTemplateFromURL':s3url}, 'Type': 'CLOUD_FORMATION_TEMPLATE'},IdempotencyToken='santoshchituprolu')
  print response
 
if __name__ == "__main__":
   main(sys.argv[1:])
