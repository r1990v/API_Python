#!/usr/local/bin/python2.7
import boto3
import sys

instanceIdsStop = ["i-xxxxxxxxxxxxxxxxx","i-xxxxxxxxxxxxxxxxx"]

action = "JumpServer Environment"
def main():
# read arguments from the command line and
# check whether at least two elements were entered
    if len(sys.argv) < 2:
        print "Usage: python aws.py {start|stop}\n"
        sys.exit(0)
    else:
        action = sys.argv[1]
        print(sys.argv[1])
        for i,item in enumerate(instanceIdsStop):
            client= boto3.client('ec2',region_name='us-east-1')
            if "stop" == sys.argv[1]:
                client.stop_instances(InstanceIds=[instanceIdsStop[i]])
                waiter=client.get_waiter('instance_stopped')
                waiter.wait(InstanceIds=[instanceIdsStop[i]])
                print(instanceIdsStop[i] +" Got stopped " +action )
            else:
                client.start_instances(InstanceIds=[instanceIdsStop[i]])
                print(instanceIdsStop[i] +"started " + action)
