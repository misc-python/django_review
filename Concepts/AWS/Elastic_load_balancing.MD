# AWS Elastic Load Balancing: Distribute Traffic

## What Is Elastic Load Balancing

Elastic Load Balancing is designed for optimal traffic distribution.

ELB automatically “load balances” incoming application traffic across multiple “targets” (eg, servers) so that no one resource becomes over burdened.  The targets can be EC2 instances, containers, and IP addresses, and can handle varying loads of application traffic in a single or multiple Availability Zones.


## Classic Load Balancer:

It distributes traffic across multiple EC2 instances.


## Application Load Balancer:

It balances HTTP and HTTPS traffic, providing advanced request routing. It routes traffic to targets within Virtual Private Cloud based on the request content.


## Network Load Balancer:

It's the best for distributing TCP traffic, and is optimized to handle sudden and volatile traffic patterns. It handles millions of requests per second, routing traffic to targets within VPC.


Source: https://awsnewbies.com/elastic-load-balancing/



# Virtual Private Cloud (VPC)

## What Is Virtual Private Cloud

Amazon Virtual Private Cloud (VPC) is a networking service, where you can create a private virtual network within the AWS cloud infrastructure,isolated from the rest of AWS.

