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
			os.system("yum install httpd")
		elif int(ch) == 4:
			print("Enter the UserName: ",end=' ')
			userName = input()
			os.system("ssh {0} useradd {1}".format(remoteIP,userName))
		elif int(ch) == 5:
			print("Enter The File Name: ",end=' ')
			file_name = input()
			os.system("mkdir {}".format(file_name))
		elif int(ch) == 6:
			os.system("date")
		elif int(ch) == 7:
			print("Enter the Software Name: ",end=' ')
			software_name = input() 
			os.system("rpm -q {}".format(software_name))
		elif int(ch) == 8:
			exit()
		else: 	
			print("Invalid Choice!!")

	else:
		print("Location not supported!!")











