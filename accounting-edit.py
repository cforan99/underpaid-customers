
MELON_COST = 1.00
FANCY_LINE = "**********  "

def underpayment_report(filename="customer-orders.txt"):
	""" Takes a text file of customer order information, iterates over each line to find
	the customer name, melon quantitity, and amount payed, determines if the customer 
	underpaid and prints a report listing those customers and the amount they owe.
	"""

	print FANCY_LINE, "CUSTOMERS WHO UNDERPAID", FANCY_LINE

	customer_orders_file = open("customer-orders.txt")

	for line in customer_orders_file:
		payment_info = line.split("|")
		customer_id, customer_name, melon_qty, customer_payment = payment_info
		expected_payment = MELON_COST * int(melon_qty)
		if float(customer_payment) < expected_payment:
			underpayment_amount = expected_payment - float(customer_payment)
			print "{} underpaid by ${:.2f}".format(customer_name, underpayment_amount)

	customer_orders_file.close()


def overpayment_report(filename="customer-orders.txt"):
	""" Takes a text file of customer order information, iterates over each line to find
	the customer name, melon quantitity, and amount payed, determines if the customer 
	overpaid and prints a report listing those customers and the amount we owe them.
	"""

	print FANCY_LINE, "CUSTOMERS WHO OVERPAID", FANCY_LINE

	overpaid_customers_count = 0

	customer_orders_file = open("customer-orders.txt")
	
	for line in customer_orders_file:
		payment_info = line.split("|")
		customer_id, customer_name, melon_qty, customer_payment = payment_info
		expected_payment = MELON_COST * int(melon_qty)		
		if float(customer_payment) > expected_payment:
			overpayment_amount = float(customer_payment) - expected_payment
			print "{} overpaid by ${:.2f}".format(customer_name, overpayment_amount)
			overpaid_customers_count += 1	

	if overpaid_customers_count == 0:
		print "No customers overpaid."

	customer_orders_file.close()

underpayment_report()
overpayment_report()


