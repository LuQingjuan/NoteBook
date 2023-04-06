* Type:
* Tags:
* Date: 2023-03-29 09:52:17
* Related:
* Reference:[]()

## Amazon EC2
* EC2 is one of the most popular of AWS’ offering 
* EC2 = Elastic Compute Cloud = Infrastructure as a Service
* It mainly consists in the capability of :
  * Renting virtual machines (EC2)
  * Storing data on virtual drives (EBS)
  * Distributing load across machines (ELB)
  * Scaling the services using an auto-scaling group (ASG)
* Knowing EC2 is fundamental to understand how the Cloud work

一台虚拟机
EC2 sizing & configuration options
* Operating System (OS): Linux, Windows or Mac OS
* How much compute power & cores (CPU)
* How much random-access memory (RAM)
* How much storage space:
  * Network-attached (EBS & EFS)
  * hardware (EC2 Instance Store)
* Network card: speed of the card, Public IP address
* Firewall rules: security group
* Bootstrap script (configure at first launch): EC2 User Dat

* All **inbound** traffic is **blocked** by default
* All **outbound** traffic is **authorised** by default


Classic Ports to know
* 22 = SSH (Secure Shell) - log into a Linux instance
* 21 = FTP (File Transfer Protocol) – upload files into a file share
* 22 = SFTP (Secure File Transfer Protocol) – upload files using SSH
* 80 = HTTP – access unsecured websites
* 443 = HTTPS – access secured websites
* 3389 = RDP (Remote Desktop Protocol) – log into a Windows instanc