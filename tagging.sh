#!/bin/bash

TAG_KEY="Environment"
TAG_VALUE="Production"

INSTANCES=$(aws ec2 describe-instances --query "Reservations[*].Instances[*].[InstanceId]" --output text)

for INSTANCE in $INSTANCES; do

  TAGS=$(aws ec2 describe-tags --filters "Name=resource-id,Values=$INSTANCE" --query "Tags")

  if [ "$TAGS" == "[]" ]; then
    echo "Instance $INSTANCE has no tags. Tagging it with $TAG_KEY=$TAG_VALUE"
    
    aws ec2 create-tags --resources $INSTANCE --tags Key=$TAG_KEY,Value=$TAG_VALUE
  else
    echo "Instance $INSTANCE is already tagged."
  fi
done

echo "Tagging complete."
