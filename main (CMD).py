import os
import inquirer

test1 = True
art2=('''   
   __    _    _  ___     ___  __    ____ 
  /__\  ( \/\/ )/ __)   / __)(  )  (_  _)
 /(__)\  )    ( \__ \  ( (__  )(__  _)(_ 
(__)(__)(__/\__)(___/   \___)(____)(____)
''')
def aws_cli():
  questions = [
    inquirer.List('choice',
                  message="What do you want to do?",
                  choices=['Install AWS CLI','Create a Key Pair','Launch your Instance ', 'Create a bucket','Sync bucket','Status','exit',],
              ),
  ]
  answers = inquirer.prompt(questions)
  test=str(answers)
  #print(test)
  
  if test == "{'choice': 'Create a Key Pair'}":
    MyKeyPair =input("Enter your keypair name:")
    keypaircommand = (f"aws ec2 create-key-pair --key-name {MyKeyPair} --query 'KeyMaterial' --output text > {MyKeyPair}.pem")
    print(keypaircommand)
    os.system('cmd /k'+keypaircommand)

#install AWS Cli
  elif test == "{'choice': 'Install AWS CLI'}":
      
      #print('hi install')
      installcli= f"msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi"
      os.system('cmd /k'+ installcli)
      install2=f"aws --version"
      install3=f"aws configure"
      os.system('cmd /k'+ install2)
      os.system('cmd /k'+ install3)
      

  #Launch Instance
  elif test == "{'choice': 'Launch your Instance '}":
    keypair=input("Enter your keypair:")
    ami=input("Enter AMI ID(eg:ami-xxxxxxxx):")
    ec2command = (f"aws ec2 run-instances --image-id{ami}--count 1 --instance-type t2.micro --key-name {keypair} --security-group-ids sg-903004f8 --subnet-id subnet-6e7f829e") 
    print(ec2command)
    os.system('cmd /k'+ec2command) 
    os.system('aws ec2 describe-key-pairs')
  
    
  #create bucket
  elif test == "{'choice': 'Create a bucket'}": 
    bucketname=input("Enter bucketname you want to create:")
    bucketcommand=f"aws s3 mb s3://{bucketname}"
    print(bucketcommand)
    bucketcommand1 ="aws s3 ls"
    os.system('cmd /k'+ bucketcommand)  
    os.system('cmd /k'+ bucketcommand1)
  
  #sync buckets
  elif test == "{'choice': 'Sync bucket'}": 
    bucketpath=input("Enter bucketname path to sync:")
    localpath=input("Enter local path to sync:")
    bucketpathcommand=f"aws s3 sync {localpath} s3://{bucketpath}"
    print(bucketpathcommand)
    os.system(bucketpathcommand)  
  
  elif test == "{'choice': 'exit'}": 
    
    print('''
|~)| _  _  _ _    _| _  _ _|_   _  _ | 
|~ |(/_(_|_\(/_  (_|(_)| | |   (_|(_).
                                _|  
								
								''')
    exit()

#status  

  elif test == "{'choice': 'Status'}": 
    questions = [
    inquirer.List('choice1',
                  message="What do you want to do?",
                  choices=['AWS S3 Bucket Status','EC2 Instant Staus',],
              ),
  ]
  answers1 = inquirer.prompt(questions)
  status1=str(answers1)
  
  if status1 == "{'choice1': 'AWS S3 Bucket Status'}": 
    print("list of S3 Buckets")
    bucketcommand2 ="aws s3 ls"
    os.system(bucketcommand2)
    
  elif status1 == "{'choice1': 'EC2 Instant Staus'}": 
      print("instant")
      os.system('aws ec2 describe-key-pairs')
    
while test1:
  aws_cli()

  

 



