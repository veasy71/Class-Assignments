# Terriyon Antonio Veasy
# Bill Reuben
# Computer Logic
# 05.12.2022
#Employee/Salary
	#Input a list of employee names and salaries and store them in parallel arrays.  End the input with a sentinel value. The salaries should be floating point numbers  
	#Salaries should be input in even hundreds.  For example, a salary of 36,510 should be input as 36.5 and a salary of 69,030 should be entered as 69.0. 
	#Find the average of all the salaries of the employees.  Then find the names and salaries of any employee who's salary is within 5,000 of the average.  
	#So if the average is 30,000 and an employee earns 33,000, his/her name would be found.

		#Global Variables
emp_names_and_salary = {} #using dictionary to store employee names and salary
total = 0.0 # totals all salary together to find averages
average = 0.0
diference = 0.0
within_five_thousand = {}

#gets user input the salary
def get_salary():
	salary = float(input("How much does this employee make: "))
	return(salary)
#gets user input the employee name
def get_employee():
	employee = input("What is the employee's name, if there is no other employee comment done: ")
	return(employee)
# used to find the average salary in our database
def find_average(emp_names_and_salary, total):
	average = total/len(emp_names_and_salary)
	return(average)
# finds the total of salaries which is later used to find averages
def find_total(emp_names_and_salary, total):
	for key, value in emp_names_and_salary.items():
		total = total + value
	return(total)
# tells if the difference from average and salary is within the given range then returns boolean value 
def is_salary_within_five_thousand(salary, average):
	if salary - average <= 5.0 and salary - average >= 0:
		return True
	if average - salary <= 5.0 and average - salary >= 0:
		return True
	return False
#This function makes the new dictionary with the employee's names and salaries that are within the specified range
def find_salaries_within_five_thousand(emp_names_and_salary, average, within_five_thousand):
	for employee, salary in emp_names_and_salary.items():
		if(is_salary_within_five_thousand(salary, average) == True):
			within_five_thousand.update({employee:salary})
	return(within_five_thousand)
# returns boolean value test's if sentinel value was added to the dictionary and if so ends the program
def is_new_employee(employee):
	if employee == "done":
		return False
	return True
#will satisfy base case of empty dictionary* without this function program would crash
def is_empty_dictionary(emp_names_and_salary):
	if len(emp_names_and_salary) == 0:
		return True
	return False
# Function calls
employee = get_employee()
new_employee = is_new_employee(employee)
# This part may be redundant and in need of refactoring, put recalls the functions until user determines there is no more employees to add
while is_new_employee(employee) == True:
	salary = get_salary()
	emp_names_and_salary.update({employee:salary})
	employee = get_employee()
# also may be redundant, but tests these functions are called only if the dictionary has elements in them other than "done"
if is_empty_dictionary(emp_names_and_salary) == False:
	total = find_total(emp_names_and_salary,total)
	average = find_average(emp_names_and_salary, total)
	within_five_thousand = find_salaries_within_five_thousand(emp_names_and_salary, average, within_five_thousand)

for employee, salary in within_five_thousand.items():
	salary = int(salary)
	salary = salary * 1000
	within_five_thousand.update({ employee: salary})
#Print functions for desired output

print("Here is your database of employees and their listed salaries")
print(emp_names_and_salary)
print("Your average salary among your employees are: ", average)
print("And all your employees who are within five thousand of the salary and their corresponding salaries are: ")
print(within_five_thousand) 