# 2018 comments

print ("A stupid square root calculator.")
var1 = float(input("Value?\n"))
i = 1 # this hurts my soul
guessnumber = 0
approach = 0 # What was I thinking, I'm using integer truthiness in this scenario, just very very wrongly.
while True : # What is this C or something
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

# Overall the algorithm I chose to do this isn't HALF bad, but the implementation just shows that I only knew some basic C at the time.
