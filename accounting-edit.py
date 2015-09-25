
customer_orders_file = open("customer-orders.txt")

MELON_COST = 1.00
FANCY_LINE = "**********  "

def underpayment_report(filename="customer-orders.txt"):

	print FANCY_LINE, "CUSTOMERS WHO UNDERPAID", FANCY_LINE
	customer_orders_file = open("customer-orders.txt")
	for line in customer_orders_file:
		payment_info = line.split("|")
		customer_number, customer_name, melon_qty, customer_payment = payment_info
		expected_payment = MELON_COST * int(melon_qty)
		if float(customer_payment) < expected_payment:
			underpayment_amount = expected_payment - float(customer_payment)
			print "{} underpaid by ${}".format(customer_name, underpayment_amount)

def overpayment_report(filename="customer-orders.txt"):

	print FANCY_LINE, "CUSTOMERS WHO OVERPAID", FANCY_LINE

	overpaid_customers_count = 0

	customer_orders_file = open("customer-orders.txt")
	for line in customer_orders_file:
		payment_info = line.split("|")
		customer_number, customer_name, melon_qty, customer_payment = payment_info
		expected_payment = MELON_COST * int(melon_qty)		
	if float(customer_payment) > expected_payment:
		overpayment_amount = float(customer_payment) - expected_payment
		print "{} overpaid by ${}".format(customer_name, overpayment_amount)
		overpaid_customers_count += 1

	if overpaid_customers_count == 0:
		print "No customers overpaid."


underpayment_report()
overpayment_report()


