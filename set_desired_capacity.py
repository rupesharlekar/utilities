#!/usr/bin/python
import boto3
import sys
import logging


def make_desired_capacity_zero(autoScalingGroupName):
    autoscaling_client = boto3.client('autoscaling')

    try:
        response = autoscaling_client.set_desired_capacity(
            AutoScalingGroupName=autoScalingGroupName,
            DesiredCapacity=0,
            HonorCooldown=False
        )
    except Exception as e:
        logging.error(e)
        # print(e)
        return None

    # print("\nResponse for set_desired_capacity method:\n", response)
    logging.info(f'Response for set_desired_capacity method {response}')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # region = ""
    autoScalingGroupName = sys.argv[1]

    make_desired_capacity_zero(autoScalingGroupName)