#!/usr/bin/python
import boto3
import sys


def make_desired_capacity_zero(autoScalingGroupName):
    try:
        autoscaling_client = boto3.client('autoscaling')

        response = autoscaling_client.update_auto_scaling_group(
            AutoScalingGroupName=autoScalingGroupName,
            MinSize = 0,
            MaxSize = 0,
            DesiredCapacity = 0,
            DefaultCooldown = 0,
        )
    except Exception as e:
        print(e)
        return None

    print("Response for set_desired_capacity method:", response)

if __name__ == "__main__":

    # region = ""
    autoScalingGroupName = sys.argv[1]

    make_desired_capacity_zero(autoScalingGroupName)