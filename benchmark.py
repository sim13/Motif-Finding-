
import random
userInput1 =input("Enter ml value \n")
userInput2 =input("Enter nm value \n")
userInput3 = input("Enter sl value\n")
userInput4 = input("Enter sc value\n")

try :
	ml = int(userInput1)
	nm = int(userInput2)
	sl = int(userInput3)
	sc = int(userInput4)
except ValueError :
	print("Enter val again")
else : 
	print("Good")

print random.sample(range(1, 500), sc)
