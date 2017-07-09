#!/usr/bin/python

import boto3

region='ap-southeast-2'
instances = []

def get_instances(instances):

  client = boto3.client('ec2')
  response = client.describe_tags(Filters=[{ 'Name': 'resource-type', 'Values': ['instance'] , 'Name': 'value', 'Values': ['EveryDay'] }])
  for i in range(len(response['Tags'])):
    if response['Tags'][i]['ResourceType'] == 'instance':
      instances.append(str(response['Tags'][i]['ResourceId']))

def lambda_handler(event, context):
   
    get_instances(instances)

    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    print 'stopped your instances: ' + str(instances)

