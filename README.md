# AWS

- OpenVPN.txt

	This Cloud Formation template to make OpenVPN instance up and running.
	Before using the template you may need to update the respective region that you are trying to deploy in along with AMI images ID's.

- VPC_Formation.txt
	1) CF Template creates VPC with 2 subnets ( public + private ) in AZ1 and 2 more subnets ( public + private ) subnets in AZ2.
	2) Creates NAT Gateway in public subnet of AZ1.
	3) Creates Route tables public and private.
	4) Create Internet Gateway and attach to VPC.
	5) Update public route table with the route to IGW.
	6) Update private route table with the route to NAT Gateway.
	7) Creates public and private ACL tables.
	
