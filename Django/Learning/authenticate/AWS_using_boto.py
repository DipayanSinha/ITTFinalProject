#!/usr/bin/env python
import boto3
import json
from . import configuration

access_key = configuration.ACCESS_KEY
secret_key = configuration.SECRET_KEY

def establish_connection(access_key,secret_key):
    global connection
    connection = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name='us-west-2')

def retrieve_instances():
    connection = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name='us-west-2')
    ec2_regions = [region['RegionName'] for region in connection.describe_regions()['Regions']]
    return ec2_regions
    '''count = [0 for i in range(len(ec2_regions))]
    ctr=0
    print("Instance ID\t\tIntsance State")
    L = []
    for region in ec2_regions:
        conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name=region)
        instances = conn.instances.filter()
        for instance in instances:
            if instance.state["Name"] == "stopped":
                print(instance.id, instance.instance_type, region)
                count[ctr]+=1
        L.append([region, count[ctr]])
        ctr+=1

    return L'''

def retrieve_instance_from_region(location):
    establish_connection(access_key, secret_key)
    conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=location)
    instances = conn.instances.filter()
    ctr_stopped = 0
    ctr_running = 0
    for instance in instances:
        if instance.state["Name"] == "stopped":
            print(instance.id, instance.instance_type, location)
            ctr_stopped+=1
        elif instance.state["Name"] == "running":
            print(instance.id, instance.instance_type, location)
            ctr_running+=1
    message_running = "No. of Running Instances: "+str(ctr_running)
    message_stopped = "No. of Stopped Instances: "+str(ctr_stopped)
    return message_running,message_stopped

def show_buckets():
    connection = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                                 region_name='us-west-2')
    s3 = boto3.resource('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name='us-west-2')
    L = []
    try:
        response = connection.list_buckets()
        for bucket in response['Buckets']:
            print(bucket['Name'])
            bucket_region = s3.Bucket(bucket['Name'])
            region_name = s3.meta.client.get_bucket_location(Bucket=bucket_region.name)["LocationConstraint"]
            print(region_name)
            L.append([bucket['Name'],region_name])
    except:
        print("The bucket does not exist, choose how to deal with it or raise the exception: ")
    return L

#show_buckets()
#retrieve_instance_from_region("us-west-2")
#establish_connection(access_key,secret_key)
#retrieve_instances()
