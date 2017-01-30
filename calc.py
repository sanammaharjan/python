# Starting Calculator Programming
print("Welcome to Python Calculator")
ans=input('''Are you ready? 
	Press "Y" if you are interested
	Press "N" if you want to quit
	Answer: ''')
#n1=input("Write your first number: ")
#op=input('''Pleae type your operator
#	+ for addition
#	- for substraction
#	* for multiplication
#	/ for division 
#	Your operator is : ''')

def calculate():
	n1=int(input("Write your first number: "))
	op=input('''Pleae type your operator
	+ for addition
	- for substraction
	* for multiplication
	/ for division 
	Your operator is : ''')
	n2=int(input("Your your second number:"))
	sum=n1+n2
	sub=n1-n2
	mul=n1*n2
	div=n1/n2
	
	if op=="+":
		print ("Your answer is = " + str(sum))
	elif op=="-":
		print ("Your answer is = " + str(sub))
	elif op=="*":
		print ("Your answer is = " + str(mul))
	elif op=="/":
		print ("Your answer is = " + str(div))
	else:
		print("Choose the right operator")
	print()
	print()
	acal()
	
def acal():
	again=input('''Would you like to do it again, Type
	"Y" for Yes
	or
	"N" for No : ''')
	if again=="Y" or again=="y":
		calculate()
	elif again=="N" or again=="n":
		exit()
	else:
		print("Please choose the right answer")
		acal()
	
if ans=="Y" or ans=="y":
	calculate()
else:
	exit()

