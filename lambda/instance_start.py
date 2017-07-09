#!/usr/bin/python

import boto3
import time

region='ap-southeast-2'

def get_instances(instances):

  client = boto3.client('ec2')
  response = client.describe_tags(Filters=[{ 'Name': 'resource-type', 'Values': ['instance'] , 'Name': 'value', 'Values': ['EveryDay'] }])
  for i in range(len(response['Tags'])):
    if response['Tags'][i]['ResourceType'] == 'instance':
      instances.append(str(response['Tags'][i]['ResourceId']))

def bastion_host(bastion):

  client = boto3.client('ec2')
  response = client.describe_instances(Filters=[{ 'Name': 'tag:Name', 'Values': ['Bastion'] }])
  while not response['Reservations'][0]['Instances'][0]['PublicDnsName']:
    time.sleep(15)
  return response['Reservations'][0]['Instances'][0]['PublicDnsName']

def linuxndevops(ip):

  client = boto3.client('ec2')
  response = client.describe_instances(Filters=[{ 'Name': 'tag:Name', 'Values': ['Course1'] }])
  while not response['Reservations'][0]['Instances'][0]['PublicDnsName']:
    time.sleep(15)
  return response['Reservations'][0]['Instances'][0]['PublicIpAddress']

def update_rr(bastion,ip):

  client = boto3.client('route53')
  response = client.list_hosted_zones()
  for i in range(len( response['HostedZones'])):
    if response['HostedZones'][i]['Name'] == 'linuxndevops.com.':
      update_host_response = client.change_resource_record_sets(  HostedZoneId=response['HostedZones'][i]['Id'], ChangeBatch={'Changes': [{ 'Action': 'UPSERT', 'ResourceRecordSet': { 'Name': 'ssh.linuxndevops.com.', 'Type': 'CNAME', 'TTL': 300, 'ResourceRecords': [{'Value': bastion }] } } ]})
      update_ip_response = client.change_resource_record_sets(  HostedZoneId=response['HostedZones'][i]['Id'], ChangeBatch={'Changes': [{ 'Action': 'UPSERT', 'ResourceRecordSet': { 'Name': 'linuxndevops.com.', 'Type': 'A', 'TTL': 300, 'ResourceRecords': [{'Value': ip }] } } ]})

def lambda_handler(event, context):

    instances = []
    bastion = ''
    ip = ''

    get_instances(instances)

    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print 'started your instances: ' + str(instances)

    bastion = bastion_host(bastion)
    ip = linuxndevops(ip)
    update_rr(bastion,ip)

