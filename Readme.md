# Deployment Steps

1. compiling
   `sam build`
1. package
   `sam package -t template.yaml --s3-bucket seto-cloudformation-play --output-template-file finalTemplate.yaml --config-file ./samconfig.toml --config-env test`
1. verification (only upload the changeset but changes are not deployed)
   `aws cloudformation deploy --capabilities CAPABILITY_IAM --template-file ./finalTemplate.yaml --stack-name seto-test-stack --no-execute-changeset`
1. deployment with specified role
   `aws cloudformation deploy --capabilities CAPABILITY_IAM --template-file ./finalTemplate.yaml --stack-name seto-test-stack`
