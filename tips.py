from decimal import *

dollar_sign, total_before_tip = input("How much was your bill?").split("$", 1)

tip_15 = float(total_before_tip) * .15
tip_18 = float(total_before_tip) * .18
tip_20 = float(total_before_tip) * .20

print("""Your suggested tip amounts are: 
	%.2f
	%.2f
	%.2f
	""" % (tip_15, tip_18, tip_20))

