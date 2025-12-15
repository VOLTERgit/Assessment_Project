import random

standard_rooms = 5
deluxe_rooms = 3
suite_rooms = 2
user_name = "" 
contact_t1 = 0
dic = {}

def book_room():
	global standard_rooms, deluxe_rooms, suite_rooms, user_name, user_contact_number, number_of_nights, dic
	booking_loop = True
	while booking_loop:
		room_types = """
			Standard : ₹2,000/night
			Deluxe : ₹3,500/night
			Suite : ₹4,500/night
			wirte 'exit' for exit...
		"""

		print(room_types)
		room_types_input = input("Enter Your Room Choice: ")
		name_t1 = str(input("Enter Your Full Name: "))
		contact_t1 = input("Enter Your Mobile Number: ")
		c1 = len(contact_t1)
		while c1 != 10:
			print("Invalid Contact Number..!! Please Enter 10 digit mobile number ..!!")
			contact_t1 = input("Enter Your Mobile Number: ")
			c1 = len(contact_t1)	
		nights_t1 = int(input("Enter Number Of Night: "))
		number_of_nights = nights_t1
		print(f"How many rooms you want: we have {standard_rooms} rooms")
		number_of_rooms = int(input("Enter: "))
		
		dic ["name"] = name_t1
		dic ["Contact_no"] = contact_t1
		dic ["nights"] = nights_t1
		dic ["numbers_rooms"] = number_of_rooms

		print(room_types_input)
		if room_types_input.lower() == "standard":
			
			if number_of_rooms <= standard_rooms:
				
				standard = 2000
				amount = standard * number_of_nights * number_of_rooms
				dic["Total_Amount"]  = amount
				print(f"{dic}")
				standard_rooms -= number_of_rooms
				
			
			else:
				print("Sorry but we have just 5 Standard rooms: ")


		elif room_types_input.lower() == "deluxe":
			if number_of_rooms <= deluxe_rooms:
				delux = 3500
				ans_deluxe = delux * number_of_nights * number_of_rooms 
				print(f"Your Total Cost : {ans_deluxe}")
				deluxe_rooms -= number_of_rooms

			else:
				print("Sorry but we have just 5 Deluxe rooms: ")


		elif room_types_input.lower() == "Suite":
			if number_of_rooms <= deluxe_rooms:
				suite = 4500
				ans_suite = suite * number_of_nights * number_of_rooms 
				print(f"Your Total Cost : {ans_suite}")
				suite_rooms -= number_of_rooms
			else:
				print("Sorry but we have just 5 Standard rooms: ")
		else:
			print("Exit !!")
			break
		print(f"Your Total Cost : {dic["Total_Amount"]}")
		payment_mode = ("confirmation of the booking, please proceed to payment.")
		print(payment_mode)
		payment_mode_1 = int(input("Enter total payment 'amount': "))
		if payment_mode_1 == dic["Total_Amount"]:
			print("Payment Successful !!")
			a = random.sample(range(1, 9), 4)
			dic["booking ID "] = a
			print(f"Your Booking ID is : {a}")
		else:
			print("Invalid Input")
	

def View_Booking():
	global standard_rooms, deluxe_rooms, suite_rooms, user_name, user_contact_number, number_of_nights, dic

	for key, value in dic.items():
			print(key," - ",value)

def Cancel_Booking():
	global standard_rooms, deluxe_rooms, suite_rooms, user_name, user_contact_number, number_of_nights, dic

	cancel_contact = input("Enter Your Mobile: ")
	cancel_booking_id = input("Enter Your Booking ID: ")
	if contact_t1 == cancel_contact & dic["booking ID "] == cancel_booking_id:
		dic.pop["name"]
		dic.pop["Contact_no"]
		dic.pop["nights"]
		dic.pop["numbers_rooms"]
		print("successfully cancel your booking")
	else:
		print("Invalid Contact Number or Booking ID")
	

status = True
while status:
	booking_types = """
		1 ... For Room Booking
		2 ... For View Booking
		3 ... For Cancel Booking
		4 ... For Exit
	"""
	print(booking_types)
	booking_types_input = input("Enter: ")
	if booking_types_input == "1":
		book_room()
	elif booking_types_input == "2":
		View_Booking()
	elif booking_types_input == "3":
		Cancel_Booking()
	elif booking_types_input == "4":
		break


	