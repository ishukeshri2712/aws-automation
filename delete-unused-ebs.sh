#!/bin/bash

# Get a list of all EBS volumes
volumes=$(aws ec2 describe-volumes --query 'Volumes[?State==`available`].VolumeId' --output text)

# Iterate over each volume
for volume in $volumes; do
    # Check if the volume is attached to an instance
    attached_instance=$(aws ec2 describe-volumes --volume-ids $volume --query 'Volumes[0].Attachments[0].InstanceId' --output text)

    if [ "$attached_instance" == "None" ]; then
        # Volume is not attached, safe to delete
        echo "Deleting volume $volume"
        aws ec2 delete-volume --volume-id $volume
    else
        echo "Skipping volume $volume as it is attached to instance $attached_instance"
    fi
done
