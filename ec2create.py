# Complete code to create a new EC2 instance
# It uses the parameters from AWS configure - access keys, etc...
# Review the instance names, types, AMI before submmiting
# It uses the key pair created in the previous step

import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-006dcf34c09e50022',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='ABKeyPairIIOpenSSH',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'EC2Imalafaia'
                    },
                ]
            }
        ]
    )

# print instance details

print(instance[0].id)
print(instance[0].instance_type)
print(instance[0].public_dns_name)
print(instance[0].public_ip_address)
print(instance[0].key_name)
print(instance[0].state)
print(instance[0].tags)
print(instance[0].launch_time)
print(instance[0].private_ip_address)
print(instance[0].security_groups)
print(instance[0].vpc_id)
print(instance[0].subnet_id)
print(instance[0].placement)
print(instance[0].monitoring)
print(instance[0].ebs_optimized)
print(instance[0].iam_instance_profile)
print(instance[0].kernel_id)
print(instance[0].ramdisk_id)
print(instance[0].block_device_mappings)
print(instance[0].network_interfaces)
print(instance[0].source_dest_check)
print(instance[0].hypervisor)