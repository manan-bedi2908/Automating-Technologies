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

def change_directory():
	directory_path = input("Enter the path of the directory you want to move on: ")
	try:
		os.system(f"cd {directory_path}")	
	except Exception as e:
		print("You have entered Invalid Directory Path!! Try again!!")
		print(e)
	else:
		os.system("tput setaf 8")
		print(f"Successfully changed the directory. Now, you are in {directory_path}")

def create_directory():
	current = input("Do you want to create a directory here only (Y/N): ")
	if current == "N":
		change_directory()
	name_dir = input("Enter the Name of the Directory: ")
	try:
		os.system(f"mkdir {name_dir}")
	except Exception as e:
		print("Error Occurred!! Not able to create a directory")
		print(e)
	else:
		os.system("tput setaf 8")
		print(f"Successfully created a Directory named {name_dir}")
		
def web_server_config():
	os.system("yum install httpd")			
	print("Apache Web Server Installed")
	os.system("systemctl start httpd")
	print("Web Server Started")
	os.system("cd /var/www/html")

def create_new_user():
	print("Enter the UserName: ",end=' ')
	userName = input()
	os.system("useradd {}".format(userName))
	print("Enter the password", end=' ')
	password = input()
	os.system("passwd {}".format(userName))

def create_file():
	print("Enter The File Name: ",end=' ')
	file_name = input()
	os.system("touch {}".format(file_name))

def check_software():
	print("Enter the Software Name: ",end=' ')
	software_name = input() 
	os.system("rpm -q {}".format(software_name))

def install_software():
	print("Enter the Software Name: ", end=' ')
	software_name = input()
	os.system("yum install {}".format(software_name))

def launch_container():
	print("Enter the Operating System Name (Operating System:version): ", end='')
	os_name = input()
	os.system("docker pull {}".format(os_name))
	print("Pulled the container image successfully from Docker Container")			
	os.system("docker run -it {}".format(os_name))
	print("Entered into the Docker Container")

def create_instance():
	image_id = input("Enter the Image ID: ")
	instance_type = input("Enter Instance Type: ")
	count = int(input("Enter the Number of Instances you want to launch: "))
	subnet_id = input("Enter the Subnet ID: ")
	sg_group_id = input("Enter the Security Group ID: ")
	key_name = input("Enter the Key Name: ")
	os.system(f"aws ec2 run-instances --image-id {image_id} --instance-type {instance_type} --count {count} --subnet-id {subnet_id} --security-group-ids {sg_group_id} --key-name {key_name}")

def attach_EBS_Volume():
	zone = input("Enter the Availability Zone (Should be same with the instance you want to attach): ")
	size = int(input("Enter the size of the EBS Volume (In GB): "))
	os.system(f"aws ec2  create-volume --availability-zone {zone}   --size {size}")
	instance_id = input("Enter the Instance ID you wish to attach EBS Volume with: ")
	volume_id = input("Enter the Volume ID: ")
	os.system(f"aws ec2 attach-volume  --device   /dev/sdg   --instance-id  {instance_id} --volume-id {volume_id}")
	print(f"Attached EBS Volume with the Instance of {size} GB")

def create_partition():
	print("Create, Format and Mount a Partition in a Virtual Hard Disk")
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

def create_s3():
	print("Create a S3 Bucket")	
	bucket_name = input("Enter the name of the Bucket: ")
	region = input("Enter the name of the region: ")	
	os.system(f"aws s3api create-bucket --bucket {bucket_name} --region {region}")

def upload_to_S3():
	bucket_name = input("Enter the name of the Bucket: ")
	file_name = input("Enter the location of the object to be uploaded to S3 Bucket: ")
	name = input("Enter the name of the object in the S3 Bucket: ")
	os.system(f"aws s3 cp {file_name} s3://{bucket_name}/{name}")
	os.system("tput setaf 11")
	public = input("Do you want to make the file in this Bucket public (Y/N): ")
	if public == 'Y':
		os.system("aws s3api put-object-acl --bucket {bucket_name} --key pic1.jpg --acl public-read")
	print("Successfully uploaded the object to the S3 Bucket!!")

def create_cloudfront():
	print("Create a CloudFront Distribution using S3 as Origin")
	bucket_name = input("Enter the name of the Bucket: ")
	file_name = input("Enter the file name in the Bucket: ")
	os.system(f"aws cloudfront create-distribution --origin-domain-name {bucket_name}.s3.amazonaws.com --default-root-object {file_name}")

def remove_file_dir():
	file_or_dir = input("Do you want to remove a file or a directory (File/Dir): ")
	print("List of all the files/directories in the current location: \n")
	os.system("ls")
	if file_or_dir == "File":
		current = input("Is the file in current location only (Y/N): ")
		if current == "N":
			change_directory()
		file_name = input("Enter the File Name to be removed: ")
		try:
			os.system(f"rm {file_name}")
		except Exception as e:
			print("Unable to remove the file!! Try Again!!")
		else:
			print("Successfully removed the file!!")
	if file_or_dir == "Dir":
		current = input("Is the Directory in current location only (Y/N): ")
		if current == "N":
			change_directory()
		dir_name = input("Enter the Directory Name to be removed: ")
		try:
			os.system(f"rm -r {dir_name} --force")
		except Exception as e:
			print("Unable to remove the file!! Try Again!!")
		else:
			print("Successfully removed the file!!")
	
		

while True:
	
	print("1. Linux/User/File Management")
	print("2. Docker Services")
	print("3. AWS Cloud")
	print("4. Hadoop Services")
	print("5. Machine Learning")
	print("0. Exit")
	
	print("Enter Your Choice: ",end=' ')
	ch = input()


	if location == "local":
		if int(ch) == 1:	
			os.system("clear")
			os.system("tput bold")
			os.system("tput setaf 2")
			print("1. Display Date")
			print("2. Display Calender")
			print("3. Create File")
			print("4. Create New User")
			print("5. Know the Current Location")
			print("6. List all the files in the current directory")
			print("7. Change the Directory")
			print("8. Create a new Directory")
			print("9. Remove a File or a Directory")
			print("10. Copy or move a File")
			print("0. Exit")
			
			ch_linux = input("Enter your Choice: ")
			if int(ch_linux) == 1:
				os.system("date")
			elif int(ch_linux) == 2:
				os.system("cal")
			elif int(ch_linux) == 3:
				create_file()
			elif int(ch_linux) == 4:
				create_new_user()
			elif int(ch_linux) == 5:
				os.system("pwd")
			elif int(ch_linux) == 6:
				os.system("ls")
			elif int(ch_linux) == 7:
				change_directory()
			elif int(ch_linux) == 8:
				create_directory()
			elif int(ch_linux) == 9:
				remove_file_dir()
			elif int(ch_linux) == 10:
				copy_move_file()
			elif int(ch) == 0:
				exit()
			else: 	
				print("Invalid Choice!!")
			input("Enter to continue...")	
			os.system("clear")
			
		elif int(ch) == 3:
			web_server_config()
		elif int(ch) == 6:
			os.system("fdisk -l")
		elif int(ch) == 7:
			check_software()
		elif int(ch) == 8:
			install_software()
		elif int(ch) == 9:
			launch_container()
		elif int(ch) == 11:
			os.system("aws ec2 describe-instances")
		elif int(ch) == 12:
			create_instance()
		elif int(ch) == 13:
			attach_EBS_Volume()
		elif int(ch) == 14: 
			create_partition()
		elif int(ch) == 15:
			create_S3()
		elif int(ch) == 16:
			upload_to_S3()
		elif int(ch) == 17:
			create_cloudfront()
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











