import boto3

REGION = 'eu-west-2'

ec2 = boto3.client('ec2', regiona_name=REGION)

def get_ec2_info(ec2, token) -> list:
    reponse = None

    if token != None:
        reponse = ec2.describe_instances(MaxResults=5, NextToken=token)
    else:
        reponse = ec2.describe_instances(MaxResults=5)

    token = reponse.get('NextToken')

    if token == None:
        return [['Instances'][0] for i in reponse.get('Researvations')]
    else:
        result = get_ec2_info(ec2, token)
        for i in reponse.get('Reservations'):
            result.append(i)
        return result

try:
    ec2_info - get_ec2_info(ec2, token=None)
    for info_rec in ec2_info:
        id = info_rec.get('Instances')[0].get('InstanceId')
        print("Instance ID: {Instance_id}".format(instance_id=id))
except Exception as e:
    print("Error: {error}".format(error=e))
