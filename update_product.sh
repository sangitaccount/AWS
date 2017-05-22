#!/bin/bash

aws s3 cp /root/AWS/cfn-templates/AWS_EC2_Instance2.txt s3://san-cfn-templates/AWS_EC2_Instance2.txt

aws servicecatalog create-provisioning-artifact --product-id prod-lgdk3omhh2qgq --parameters Name=version2,Info={'LoadTemplateFromURL'='https://s3-ap-southeast-2.amazonaws.com/san-cfn-templates/AWS_EC2_Instance2.txt'},Type=CLOUD_FORMATION_TEMPLATE --idempotency-token string

#aws servicecatalog search-products
#aws servicecatalog list-provisioning-artifacts --product-id prod-lgdk3omhh2qgq
#aws servicecatalog delete-provisioning-artifact --product-id prod-lgdk3omhh2qgq --provisioning-artifact-id pa-iirioy2xr7eu6

