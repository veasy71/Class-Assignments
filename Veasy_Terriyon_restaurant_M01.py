#Terriyon Veasy
#Bill Reuben
#SDEV143
#08/22/2022




 #Write a program that calculates the total amount of a meal purchased at a restaurant. 
 #The program should ask the user to enter the charge for the food, 
 #then calculate the amounts of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total
def main():
	cost_of_food = get_cost_of_food()
	cost_after_tax = get_cost_after_tax(cost_of_food)
	server_tip = get_server_tip(cost_after_tax)
	total_bill = get_total(cost_after_tax,server_tip)
	print("The cost of the meal before tax is: ", cost_of_food)
	print("The cost of the meal after tax is: ", cost_after_tax)
	print("Your tip amount was: ", server_tip)
	print("The cost of the total meal is: ", total_bill)

def get_cost_of_food():
	cost_of_food = float(input("How much was the cost of your meal? "))
	return(cost_of_food)

def get_cost_after_tax(cost_of_food):
 	cost_after_tax = cost_of_food *.07 + cost_of_food
 	return(cost_after_tax)

def get_server_tip(cost_after_tax):
	server_tip = cost_after_tax*.18
	return(server_tip)

def get_total(cost_after_tax, server_tip):
	return(cost_after_tax + server_tip)

main()