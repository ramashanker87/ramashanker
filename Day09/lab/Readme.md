## Command to create cloudformation

    aws cloudformation create-stack \
    --stack-name rama-ec2-stack \
    --template-body file://rama-ec2-template.yaml \
    --capabilities CAPABILITY_NAMED_IAM \
    --profile devops

## Delete cloudformation command

    aws cloudformation delete-stack \
    --stack-name rama-ec2-stack \
    --profile devops