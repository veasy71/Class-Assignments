#Trainers//enrollees
#Terriyon Veasy
#Input is the trainer's last name and the number of new enrollees.  
#Output is the number of trainers who have enrolled members in each of three categories

#Variables: 
#			new_employee = is a boolean variable that is used to ask the user if there is a new trainer to input in dictionary
#			trainers_and_num_of_members = is a dictionary used to store the our key:value of {trainer:numofmembers}
#			trainer = the name of the trainer that is input from user
#			up_to_five_members is an int value that accumales in a while loop the number of trainers that enrolled up to five members
#			six_to_ten_members is an int value that accumalates the number of trainers that enrolled 6-10 members
#			eleven_to_fifteen_members is an int value that accumaltes the number of trainers that enrolled 11 to 15 members 

# This function will take in True or False input from user; if invalid input is entered it recurses until valid input is entered. 
#Global Variables #
up_to_five_members = 0 #
six_to_ten_members = 0 #
eleven_to_fifteen_members = 0 ####
trainers_and_num_of_members = {} #intializes dictionary#####
new_employee = True #initialize new_employee to true ###
trainer = "" # initialized to empty string
num_of_members = 0 
num_of_employees = 0
#

#Prerequisite is to test if there is the maximum amount of trainers in the list 
# will ask user input whether they would want to add another trainer into the dictionary
def isMore_trainers(num_of_employees):
	if num_of_employees >= 15:
		return False
	new_employee = input("Is there more trainers? Input True or False: ")
	if new_employee == "True":
		return True
	if new_employee == "False":
		return False
	else:	
		print("Sorry wrong value")
		isMore_trainers(num_of_employees)

# will accumulate the number employees everytime it is called
def get_num_of_employees():
	global num_of_employees #access global variable num_of_employees
	num_of_employees+=1
	return(num_of_employees)

# retrieves user input for the amount of member the trainer enrolled
def get_num_of_members():
	num_of_members = int(input("How many members enrolled? "))
	if num_of_members > 15:
		num_of_members = int(input("You're input was out of range, Try Again: "))
	return(num_of_members)

# retrieves user input; trainer's name
def get_trainers():
	trainer = input("What is the trainer's name? ")
	return(trainer)

# input: the name of the trainer and the number of members
# output: returns the new dictionary with the new trainers name and number of members add to the dictionary
def add_to_List(trainer, num_of_members):
	trainers_and_num_of_members.update({ trainer: num_of_members})
	return(trainers_and_num_of_members)

def isNewEmployee(new_employee):
	return(new_employee)

def is_up_to_five_members(value):
	if value <= 5:
		return(True)
	return(False)

def get_up_to_five_numbers(up_to_five_members):
	up_to_five_members+=1
	return(up_to_five_members)

def is_six_to_ten_members(value):
	if value >= 6 and value <= 10:
		return(True)
	return(False)

def get_six_to_ten_members(six_to_ten_members):
	six_to_ten_members+=1
	return(six_to_ten_members)

def is_eleven_to_fifteen_members(value):
	if value >= 11 and value <= 15:
		return(True)
	return(False)

def get_eleven_to_fifteen_members(eleven_to_fifteen_members):
	eleven_to_fifteen_members+=1
	return(eleven_to_fifteen_members)

def get_zero_to_five_group(trainers_and_num_of_members, up_to_five_members):
	for key, value in trainers_and_num_of_members.items():
		if is_up_to_five_members(value):
			up_to_five_members = get_up_to_five_numbers(up_to_five_members)
	return(up_to_five_members)

def get_six_to_ten_group(trainers_and_num_of_members, six_to_ten_members):
	for key, value in trainers_and_num_of_members.items():
		if is_six_to_ten_members(value):
			six_to_ten_members = get_six_to_ten_members(six_to_ten_members)
	return(six_to_ten_members)

def  get_eleven_to_fifteen_group(trainers_and_num_of_members, eleven_to_fifteen_members):
	for key, value in trainers_and_num_of_members.items():
		if is_eleven_to_fifteen_members(value):
			eleven_to_fifteen_members = get_eleven_to_fifteen_members(eleven_to_fifteen_members)
	return(eleven_to_fifteen_members)

def getEmployees(trainer, num_of_members, trainers_and_num_of_members, new_employee, num_of_employees):
	#While loop that intializes elements in dictionary
#inputs key:value elements in dictionary trainers: num_of_mebers
	while isNewEmployee(new_employee):
		trainer = get_trainers()
		num_of_members = get_num_of_members()
		trainers_and_num_of_members = add_to_List(trainer, num_of_members)
		new_employee = isMore_trainers(num_of_employees)
		num_of_employees = get_num_of_employees()
	return(trainers_and_num_of_members)

#fuction calls
trainers_and_num_of_members = getEmployees(trainer, num_of_members, trainers_and_num_of_members, new_employee, num_of_employees)		
up_to_five_members = get_zero_to_five_group(trainers_and_num_of_members, up_to_five_members)
six_to_ten_members = get_six_to_ten_group(trainers_and_num_of_members, six_to_ten_members)
eleven_to_fifteen_members = get_eleven_to_fifteen_group(trainers_and_num_of_members, eleven_to_fifteen_members)

#print fuctions
print("Ok! here is your trainers and their number of members enrolled:")
print(trainers_and_num_of_members) # Prints out key:value elements in our dictionary
#Prints out the number of trainers in each group. 
print("There is ", up_to_five_members, "in the 0-5 group.")
print("There is ", six_to_ten_members, "in the 6-10 group.")
print("There is ", eleven_to_fifteen_members, "in the 11-15 group.")