#!/usr/bin/env python

'''
File: ec2-example1.py
Author: Austin Godber
Description: Example of launching an EC2 instance with boto
'''

import boto
import time
import pprint
import sys

def main(ami_id):
    """docstring for main"""
    # Assumes these environment variables are set
    # AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
    conn = boto.connect_ec2()
    sg = conn.get_all_security_groups(['default'])
    image = conn.get_image(ami_id)
    reservation = image.run(
            security_groups = sg,
            instance_type = 't1.micro',
            key_name = 'godber-uberhip-ec2',
            )
    instance = reservation.instances[0]
    time.sleep(2)  # Eventually Consistent
    instance.update()
    while instance.state != 'running':
        instance.update()
        print "."
        time.sleep(2)
    time.sleep(5)
    instance.update()
    pprint.pprint(instance.__dict__)

if __name__ == '__main__':
    ami_id = 'ami-3e02f257'
    main(ami_id)
