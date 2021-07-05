print("Hi there, welcome back to Darko's car rentals. We hope you enjoyed your trip.\nTo pay please fill out the electronic form below.")
customers_name = input("Name: ")
print("OUR RATES: Budget is $40 per day + $0.25 per km.\nDaily is $60 per day up to 100km per day, $0.25 after.\nWeekly is $190 per week, no extra charge for first 900km, $50 charge for up to 1500km and a $100 charge + $0.25 for driving more than 1500km.")
customer_code = input("Are you selecting our budget, daily or weekly package (select B,D, or W): ")
days_rented = int(input("How many days did you have the vehicle?: "))
odometer_start = int(input("Odometer reading at start of rental: "))
odometer_end = int(input("Odometer reading at end of rental: "))
km_billed = odometer_end - odometer_start
if(customer_code == 'B'):
	cost1 = days_rented*40+km_billed*0.25
else: cost1=0
if(customer_code == 'D' and km_billed <= 100):
	cost2 = days_rented*60
elif(customer_code == 'D' and km_billed >100):
	cost2 = days_rented*60+km_billed*0.25
else: cost2 = 0
weeks_rented = days_rented/7
if(customer_code == 'W' and km_billed <= 900):
	cost3 = weeks_rented*190
elif(customer_code == 'W' and km_billed >900 and km_billed <=1500):
	cost3 = weeks_rented*240
elif(customer_code == 'W' and km_billed > 1500):
	cost3 = weeks_rented*290+km_billed*0.25
else: cost3 = 0
cost4 = cost1 + cost2 + cost3 
print("{}, you rented our car for {} days and drove a total of {}km under our package.".format(customers_name, days_rented, km_billed))
print("You will be charged $", cost4)
