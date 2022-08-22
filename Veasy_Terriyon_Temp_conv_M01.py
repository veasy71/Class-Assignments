 ,,,,#Terriyon Veasy
#Bill Reuben
#SDEV143
#08/22/2022




#Write a program that converts Celsius temperatures to Fahrenheit temperatures. 
def main():
	celsius = getCelsius()
	fahrenheit = get_fahrenheit(celsius)
	print(celsius, "converted into Fahrenheit is ", fahrenheit)
def getCelsius():
	Celsius = float(input("What is the current temperatures in Celsius?: "))
	return(Celsius)
def get_fahrenheit(celsius):
	fahrenheit = temp_conv(celsius)
	return(fahrenheit)
def temp_conv(celsius):
	temp_conv = 9/5*celsius+32
	return(temp_conv)
main()