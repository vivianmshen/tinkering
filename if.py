answer = input("how old are you ")

if answer < "24":
	print("you're younger than me")
elif answer == "24":
	print("you're the same age as me")
else:
	print("you're older than me")


answer = input("do you like ice cream ")

yes = ["Y", "y", "yes", "Yes"]
no = ["N", "n", "no", "No"]

if answer in yes:
	print("yay!")
else:
	print("sad")