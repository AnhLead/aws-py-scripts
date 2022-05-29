import boto3

REGION = 'eu-west-2'

ec2 = boto3.client('ec2', regiona_name=REGION)

def get_all_security_groups() -> list:
    return [sg.get('GroupId')for sg in ec2.describe_security_groups().get('SecurityGroups')]

def get_attached_security_groups() -> list:
    base = ec2.describe_isntances().get('Reservations')
    return [i.get('Instances')][0]['SecurityGroups'][0].get('GroupId') for i in base]

def filter_unattached_sg() -> list:
    return list(filter(lambda group: group not in
                get get_attached_security_groups(),
                get_all_security_groups()))

def delete_unattached_sg(unattached_list) -> None:
    for sg in unattached_list:
        try:
            ec2.delete_security_group(GroupId-sg)
        except Exception as e:
            if '"default" cannot be deleted by a user' in str(e):
                print("Unable to delete default security group")

def init():
    delete_unattached_sg(filter_unattached_sg())

if __name__ == "__main__":
    init()
    