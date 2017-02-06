print ("A stupid fucking square root calculator.")
var1 = float(input("Value?\n"))
i = 1
guessnumber = 0
approach = 0
while True :
	guess = i*i
	if (guess == var1) :
		break
	elif (guess <= var1) :
		if (approach == 1):
			guessnumber += 1
		i += 1/(2**guessnumber)
	elif (guess >= var1) :
		approach = 1
		guessnumber += 1
		i -= 1/(2**guessnumber)
	if (guessnumber == 20) :
		break
print ("The square root of", var1, "is approximately", round(i,4))
input("Thank you.")