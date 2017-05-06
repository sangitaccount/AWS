# AWS

- OpenVPN.txt

	This Cloud Formation template to make OpenVPN instance up and running.
	Before using the template you may need to update the respective region that you are trying to deploy in along with AMI images ID's.

- VPC_Formation.txt
	1) CF Template creates VPC with 3 subnets ( public + private ) so total in 6 in each AZ.
	2) Creates NAT Gateway in public subnet of AZ1.
	3) Creates Route tables public and private.
	4) Create Internet Gateway and attach to VPC.
	5) Update public route table with the route to IGW.
	6) Update private route table with the route to NAT Gateway.
	7) Creates public and private ACL tables.
	
- AWS_EC2_Instance
	1) Simple template to provision EC2 Instance in the selected subnet
	
- AWS_EC2_Apache
	1) Simple template to provision EC2 Instance with Apache running
