import os
import getpass

os.system("tput setaf 1")
print("\t\t\tTERMINAL USER INTERFACE")
os.system("tput setaf 7")

print("\t\t\t------------------------")

passwd = getpass.getpass("Enter the password: ")
apass = "mb"

if passwd != apass:
	print("Access Denied")
	exit()

print("Where you would like to perform your job(local/remote)?",end=' ')
location = input()
print(location)

if location == "remote":
	remoteIP = input("Enter the IP Address: ")

while True:
	print("""
Press 1: Find Date
Press 2: Check Calender
Press 3: Configure Web Server
Press 4: Create a new User
Press 5: Create File
Press 6: List the hard disks present
Press 7: Check if a Software is present
Press 8: Install a software
Press 9: Launch a Docker container
Press 10: Configure Hadoop Cluster 
Press 11: List AWS Instance
Press 12: Create and run a new EC2 Instance
Press 13: Attach EBS Volume to a EC2 Instance
Press 14: Create a Partition in a Virtual Hard Disk
Press 0: Exit
	""")

	print("Enter Your Choice: ",end=' ')
	ch = input()

	if location == "local":
		if int(ch) == 1:
			os.system("date")
		elif int(ch) == 2:
			os.system("cal")
		elif int(ch) == 3:
			os.system("yum install httpd")
			print("Apache Web Server Installed")
			os.system("systemctl start httpd")
			print("Web Server Started")
			os.system("cd /var/www/html")
		elif int(ch) == 4:
			print("Enter the UserName: ",end=' ')
			userName = input()
			os.system("useradd {}".format(userName))
			print("Enter the password", end=' ')
			password = input()
			os.system("passwd {}".format(userName))
		elif int(ch) == 5:
			print("Enter The File Name: ",end=' ')
			file_name = input()
			os.system("mkdir {}".format(file_name))
		elif int(ch) == 6:
			os.system("fdisk -l")
		elif int(ch) == 7:
			print("Enter the Software Name: ",end=' ')
			software_name = input() 
			os.system("rpm -q {}".format(software_name))
		elif int(ch) == 8:
			print("Enter the Software Name: ", end=' ')
			software_name = input()
			os.system("yum install {}".format(software_name))
		elif int(ch) == 9:
			print("Enter the Operating System Name (Operating System:version): ", end='')
			os_name = input()
			os.system("docker pull {}".format(os_name))
			print("Pulled the container image successfully from Docker Container")			
			os.system("docker run -it {}".format(os_name))
			print("Entered into the Docker Container")
		elif int(ch) == 11:
			os.system("aws ec2 describe-instances")
		elif int(ch) == 12:
			image_id = input("Enter the Image ID: ")
			instance_type = input("Enter Instance Type: ")
			count = int(input("Enter the Number of Instances you want to launch: "))
			subnet_id = input("Enter the Subnet ID: ")
			sg_group_id = input("Enter the Security Group ID: ")
			key_name = input("Enter the Key Name: ")
			os.system(f"aws ec2 run-instances --image-id {image_id} --instance-type {instance_type} --count {count} --subnet-id {subnet_id} --security-group-ids {sg_group_id} --key-name {key_name}")
		elif int(ch) == 13:
			zone = input("Enter the Availability Zone (Should be same with the instance you want to attach): ")
			size = int(input("Enter the size of the EBS Volume (In GB): "))
			os.system(f"aws ec2  create-volume --availability-zone {zone}   --size {size}")
			instance_id = input("Enter the Instance ID you wish to attach EBS Volume with: ")
			volume_id = input("Enter the Volume ID: ")
			os.system(f"aws ec2 attach-volume  --device   /dev/sdg   --instance-id  {instance_id} --volume-id {volume_id}")
			print(f"Attached EBS Volume with the Instance of {size} GB")
		elif int(ch) == 14: 
			print("Create a Partition in a Virtual Hard Disk")
			os.system("tput setaf 9")
			print("Make sure you have attached a new hard disk to the OS already")
			os.system("tput setaf 11")
			print("Displaying all the Hard Disks Available")
			os.system("fdisk -l")
			os.system("tput setaf 14")
			print("Now, create a partition in the Desired Hard Disk")
			hard_disk = input("Enter the Hard Disk: ")
			os.system("fdisk {}".format(hard_disk))
			os.system("udevadm settle")
			os.system("tput setaf 7")
			print("Driver Installed")
			partition = hard_disk + "1"
			os.system(f"mkfs.ext4 {partition}")
			os.system("tput setaf 13")
			print("Successfully formatted the Partition!!")
			folder = input("Enter the directory location to be mounted with the new partition: ")
			os.system(f"mount {partition} {folder}")
			os.system("tput setaf 7")
			os.system("Displaying the information of the disks !!")
			os.system("df -h")
		elif int(ch) == 0:
			exit()
		else: 	
			print("Invalid Choice!!")
		input("Enter to continue...")	
		os.system("clear")

	elif location == "remote":
		if int(ch) == 1:
			os.system("ssh {0} date".format(remoteIP))
		elif int(ch) == 2:
			os.system("ssh {0} cal".format(remoteIP))
		elif int(ch) == 3:				
			os.system("ssh {0} yum install httpd".format(remoteIP))
			print("Apache Web Server Installed")
			os.system("ssh {0} systemctl start httpd".format(remoteIP))
			print("Web Server Started")
			os.system("ssh {0} cd /var/www/html".format(remoteIP))
		elif int(ch) == 4:
			print("Enter the UserName: ",end=' ')
			userName = input()
			os.system("ssh {0} useradd {1}".format(remoteIP, userName))
			print("Enter the password", end=' ')
			password = input()
			os.system("ssh {0} passwd {1}".format(remoteIP, userName))
		elif int(ch) == 5:
			print("Enter The File Name: ",end=' ')
			file_name = input()
			os.system(f"ssh {remoteIP} mkdir {file_name}")
		elif int(ch) == 6:
			os.system(f"ssh {remoteIP} fdisk -l")
		elif int(ch) == 7:
			print("Enter the Software Name: ",end=' ')
			software_name = input() 
			os.system("ssh {0} rpm -q {1}".format(remoteIP, software_name))
		elif int(ch) == 8:
			print("Enter the Software Name: ", end=' ')
			software_name = input()
			os.system("ssh {0} yum install {1}".format(remoteIP, software_name))
		elif int(ch) == 9:
			print("Enter the Operating System Name (Operating System:version): ", end='')
			os_name = input()
			os.system("ssh {0} docker pull {1}".format(remoteIP, os_name))
			print("Pulled the container image successfully from Docker Container")			
			os.system("ssh {0} docker run -it {1}".format(remoteIP, os_name))
			print("Entered into the Docker Container")
		elif int(ch) == 11:
			os.system(f"ssh {remoteIP} aws ec2 describe-instances")
		elif int(ch) == 12:
			image_id = input("Enter the Image ID: ")
			instance_type = input("Enter Instance Type: ")
			count = int(input("Enter the Number of Instances you want to launch: "))
			subnet_id = input("Enter the Subnet ID: ")
			sg_group_id = input("Enter the Security Group ID: ")
			key_name = input("Enter the Key Name: ")
			os.system(f"ssh {remoteIP} aws ec2 run-instances --image-id {image_id} --instance-type {instance_type} --count {count} --subnet-id {subnet_id} --security-group-ids {sg_group_id} --key-name {key_name}")
		elif int(ch) == 13:
			zone = input("Enter the Availability Zone (Should be same with the instance you want to attach): ")
			size = int(input("Enter the size of the EBS Volume (In GB): "))
			os.system(f"aws ec2  create-volume --availability-zone {zone}   --size {size}")
			instance_id = input("Enter the Instance ID you wish to attach EBS Volume with: ")
			volume_id = input("Enter the Volume ID: ")
			os.system(f"ssh {remoteIP} aws ec2 attach-volume  --device   /dev/sdg   --instance-id  {instance_id} --volume-id {volume_id}")
			print(f"Attached EBS Volume with the Instance of {size} GB")
		elif int(ch) == 0:
			exit()
		else: 	
			print("Invalid Choice!!")
		input("Enter to continue...")	
		os.system("clear")

	else:
		print("Location not supported!!")











