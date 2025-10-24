print("TELCOS MARKET")
first_name=input("enter your first_name: ")
while first_name=="":
	print("you did not insert anything in the space")
	first_name=input("enter your first_name: ")
middle_name =input("enter your middle name: ")
while middle_name=="":
	print("you did not insert anything in the space")
	middle_name=input("enter your middle_name: ")
surname=input ("enter your surname: ")
while surname=="":
	print("you did not insert anything in the space")
	surname=input("enter your surname: ")
print("hello", first_name ,"WELCOME TO TELCOS MARKET")
while True:
    age_input = input("Enter your age: ")
    
    # Check if the input is numeric
    if age_input.isdigit():
        age = int(age_input)
        print(f"Your age is {age}")
        break
    else:
        print("Invalid input. Please enter numbers only.")
print ("your are ",age ,"years old")
email=input("enter your email address: ")
if "@" in email and ".com" in email:
	print ("your email is valid address",email)
else:
	print ("invalid email address",email)
	email = ""
while email=="":
	print("insert your email")
	email=input("enter your email_address: ")
	if "@" in email and ".com" in email:
		print ("your email is valid address",email)
	else:
		print ("invalid email address",email)
		email = ""
phone_number=input("enter your phone_number: ")
if "+254" in phone_number:
	print("valid phone_number",phone_number)
else:
	print("invalid phone_number try again",phone_number)
	phone_number=""
while phone_number=="":
	print("please insert something")
	phone_number=input("enter your phone_number: ")
	if "+254" in phone_number:
	  print("valid phone_number")
	else:
	    print("invalid phone_number")
	    phone_number=""

	
import getpass

password=getpass.getpass("enter your password: ")
while password  =="":
	print("insert something")
	password=getpass.getpass("enter your password: ")
confirm=getpass.getpass("re-enter your password: ")
while confirm=="":
	print("insert something")
	confirm =getpass.getpass("re-enter your password: ")	
#enter the website
print("welcome to telcos market")
data = input("Enter something and press Enter to submit: ")
print("You submitted:", data)